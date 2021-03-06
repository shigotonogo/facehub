# -*- coding: UTF-8 -*-
import logging
import urllib
from json import dumps
from bottle import *
from facehub.model import *
from facehub.serializer import Serializer
from facehub import storage
from facehub.image import crop_image
from datetime import date, datetime
import datetime as date_time
from playhouse.db_url import connect

app = Bottle()
TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), './templates')))
app.config.load_config('facehub.cfg')

ROLES = {
    "Professional Service": ["Dev", "DevOps", "UIDev", "BA", "QA", "UX", "Ops", "PM"],
    "Operation": ["Admin", "Finance", "IS", "HR", "Marketing", "BD", "MD", "OP", "RM", "Technical Assitant", "COO",
                  "Immigration & Mobility"]
}
OFFICES = [u"北京", u"上海", u"西安", u"成都", u"深圳", u"武汉"]

db = connect(app.config['database.url'])
initDatabase(db)
ser = Serializer()

provider = storage.provider(app.config['cloud.accesskey'], app.config['cloud.secretkey'], app.config['cloud.bucket'],
                            app.config['cloud.imageserverurl'])


@app.hook('before_request')
def before_request():
    if request.headers['host'] == 'www.facehub.net':
        redirect("%s%s" % ("http://facehub.net", request.path), 301)

    if request.path == '/login' or request.path == '/send-invitation' or request.path.startswith(
            "/assets/") or request.path == '/api/users_count' or request.path == '/verify':
        return

    token = request.get_cookie("token")
    if not token:
        redirect('/login')

    try:
        User.get(token=token)
        return
    except User.DoesNotExist:
        redirect('/login')


@app.hook('before_request')
def _connect_db():
    db.connect()


@app.hook('after_request')
def _close_db():
    if not db.is_closed():
        db.close()


@app.route('/verify')
def verify():
    def verify_token(token, email):
        response = urllib.urlopen("%s?token=%s&uid=%s" % (app.config['app.authentication'], token, email))
        try:
            status = json.loads(response.read()).get('status')
        except ValueError:
            status = 'ERROR'
        return status

    token = request.params.get('token')
    email = request.params.get('uid')
    if not token or not email:
        redirect('/login')

    token_verified_status = verify_token(token, email)
    if token_verified_status != 'OK':
        redirect('/login')

    try:
        user = User.get(email=email)
        user.token = token
        user.save()
    except User.DoesNotExist:
        user = User.create(name="", title="", birthday="", onboard="", email=email, token=token)

    response.set_cookie("token", token, max_age=60 * 60 * 24 * 7, httponly=True)
    redirect('/')


def current_user():
    return User.get(token=request.get_cookie("token"))


@app.route("/api/users", method='GET')
def users():
    response.content_type = 'application/json'
    current_month = datetime.now().month
    current_year = datetime.now().year
    query_users = [user for user in User.select() if user.completion == True]
    all_users = [ser.serialize_object(u, fields={
        User: ['id', 'name', 'avatar', 'created_at', 'onboard', 'email', 'photo', 'title', 'office', 'project']}) for u
                 in query_users]
    birthday_users = [ser.serialize_object(user, fields={
        User: ['id', 'name', 'avatar', 'created_at', 'onboard', 'email', 'title', 'office', 'project']}) for user in
                      query_users if user.birthday.month == current_month]
    anniversary_users = [ser.serialize_object(user, fields={
        User: ['id', 'name', 'avatar', 'created_at', 'onboard', 'email', 'title', 'office', 'project']}) for user in
                         query_users if (user.onboard.month == current_month) and (user.onboard.year < current_year)]
    new_users = [ser.serialize_object(user, fields={
        User: ['id', 'name', 'avatar', 'created_at', 'onboard', 'email', 'title', 'office', 'project']}) for user in
                 query_users if (user.onboard > (datetime.today() - date_time.timedelta(days=60)).date())]
    resp = {"users": all_users,
            "current_user_email": current_user().email,
            "birthday_users": birthday_users,
            "anniversary_users": anniversary_users,
            "new_users": new_users
            }
    return dumps(resp)


@app.route('/api/users/<id:int>', method='GET')
def user(id):
    response.content_type = 'application/json'
    user = User.get(User.id == id)
    if user is not None and user.completion is True:
        user.birthday = user.birthday.strftime("%-m-%-d")
        return dumps(ser.serialize_object(user, exclude={
            User: ['updated_at', 'created_at', 'id', 'avatar', 'raw_image', 'completion', 'token']}))
    else:
        abort(404, "No such user.")


@app.route('/send-invitation', method="POST")
def send_invitation():
    user_email = request.forms.getunicode('user', None)
    if user_email == None:
        abort(404, 'Missing required parameter "user".')

    data = urllib.urlencode({'user': user_email})
    response = urllib.urlopen(app.config['app.authentication'], bytearray(data, 'utf-8'))
    if response.code == 200:
        return dumps({"result": 'OK'})
    else:
        abort(500, 'Failed to send invitation.')


@app.route('/api/users', method='POST')
def createUser():
    def parse(date_str):
        return datetime.strptime(date_str, "%m/%d/%Y")

    try:
        u = current_user()

        u.project = request.forms.getunicode('project', None).strip()
        u.office = request.forms.getunicode('office', None)
        u.name = request.forms.getunicode('name', None).strip()
        u.skype = request.forms.getunicode('skype', None).strip()
        u.phone = request.forms.getunicode('phone', None).strip()
        u.title = request.forms.getunicode('title', None)
        u.birthday = parse(request.forms.getunicode('birthday', None))
        u.onboard = parse(request.forms.getunicode('onboard', None))
        u.completion = True
        u.save()
    except Exception as e:
        logging.error("can't save the user in mongo: %s" % str(e))
        return {'status': 'error',
                'message': "failed save user."}

    redirect('/')


@app.route('/upload', method='POST')
def upload():
    upload = request.files.get('file')
    image_url = provider.store(upload.file)
    try:
        user = current_user()
        user.raw_image = image_url
        user.save()
    except User.DoesNotExist:
        user = User.create(raw_image=image_url, name="", title="", birthday="", onboard="", email=email)
    return str(user.id)


@app.route("/photo")
@view("edit-photo")
def crop_photo():
    user = current_user()
    return {'image': user.raw_image + '?imageView/2/w/1200/h/1600'}


@app.route("/avatar")
@view("edit-avatar")
def crop_photo():
    user = current_user()
    return {'image': user.photo}


@app.route("/profile")
@view("edit-profile")
def crop_photo():
    user = current_user()
    birthday = datetime.strftime(user.birthday, "%m/%d/%Y") if user.birthday else ""
    onboard = datetime.strftime(user.onboard, "%m/%d/%Y") if user.onboard else ""

    return {"photo": user.photo,
            "avatar": user.avatar,
            "title": user.title or "",
            "office": user.office or "",
            "name": user.name or "",
            "phone": user.phone or "",
            "skype": user.skype or "",
            "project": user.project or "",
            "birthday": birthday,
            "roles": ROLES,
            "offices": OFFICES,
            "onboard": onboard}


@app.route('/crop', method='POST')
def editPhoto():
    img_src = request.forms.get("src", None)
    x = request.forms.get("x", None)
    y = request.forms.get("y", None)
    width = request.forms.get("w", None)
    height = request.forms.get("h", None)
    img_type = request.forms.get("image_type", None)
    img_width = request.forms.get("image_width", None)
    try:
        image = crop_image(img_src, img_width, int(round(float(x))), int(round(float(y))), int(round(float(width))),
                           int(round(float(height))))
        image_url = provider.store_file(image)

        user = current_user()
        if img_type == 'photo':
            user.photo = image_url
        if img_type == 'avatar':
            user.avatar = image_url
        user.save()
    except Exception as e:
        logging.exception("unexpected error %s" % str(e))
        abort(500, "Failed to crop image for user: %s " % email)

    return 'Success'


mimetypes = {"js": 'application/javascript', "css": "text/css", "images": "image/png"}


@app.route('/')
def index():
    return static_file("index.html", root="facehub/templates/", mimetype="text/html")


@app.route("/assets/<type>/<filename:path>")
def assets(type, filename):
    return static_file(filename, root="facehub/static/" + type, mimetype=mimetypes[type])


@app.route('/<template>')
def template(template):
    return static_file("%s.html" % template, root="facehub/templates/", mimetype="text/html")


@app.route('/login')
def login():
    return static_file("login.html", root="facehub/templates/", mimetype="text/html")


@app.route('/api/users_count')
def user_count():
    response.content_type = 'application/json'
    return {'count': User.select().where(User.completion == True).count()}


if __name__ == '__main__':
    debug(True)
    run(app=app, host='0.0.0.0', port=8080, reloader=True, server='paste')
else:
    application = app
