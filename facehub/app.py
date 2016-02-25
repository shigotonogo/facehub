import logging
import urllib
from json import dumps
from bottle import *
from model import *
from serializer import Serializer
import storage
from image import crop_image
from datetime import datetime

from playhouse.db_url import connect

app = Bottle()
TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), './templates')))
app.config.load_config('facehub.cfg')

db = connect(app.config['database.url'])
initDatabase(db)
ser = Serializer()

provider = storage.provider(app.config['cloud.accesskey'], app.config['cloud.secretkey'],app.config['cloud.bucket'], app.config['cloud.imageserverurl'])

@app.hook('before_request')
def before_request():
    if request.path == '/login' or request.path == '/send-invitation' or request.path.startswith("/assets/"):
        return
    if request.get_cookie("uid") == None:
        redirect('/login')

def current_user_email():
    return urllib.parse.unquote(request.get_cookie("uid"))

@app.route("/api/users", method='GET')
def users():
    response.content_type = 'application/json'
    current_month = datetime.now().month
    current_year = datetime.now().year
    users = User.select()
    all_users = [ser.serialize_object(u) for u in users]
    birthday_users = [ser.serialize_object(user) for user in users if user.birthday.month == current_month]
    anniversary_users = [ser.serialize_object(user) for user in users if (user.onboard.month == current_month) and (user.onboard.year < current_year)]
    resp = {"users": all_users, 
    "current_user": request.get_cookie("uid"), 
    "birthday_users": birthday_users, 
    "anniversary_users": anniversary_users}
    return dumps(resp)

@app.route('/api/users/<id:int>', method='GET')
def user(id):
    response.content_type = 'application/json'
    user = User.get(User.id == id)
    if user is not None:
        return dumps(ser.serialize_object(user))
    else:
        abort(404, "No such user.")

@app.route('/send-invitation', method="POST")
def send_invitation():
    user_email = request.forms.getunicode('user', None)
    if user_email == None:
        abort(404,'Missing required parameter "user".')

    data = urllib.parse.urlencode({ 'user': user_email })
    response = urllib.request.urlopen(app.config['app.authentication'], bytearray(data,'utf-8'))
    if response.code == 200:
        return dumps({"result":'OK'})
    else:
        abort(500, 'Failed to send invitation.')

@app.route('/api/users', method='POST')
def createUser():
    def get_date_from(date):
        return datetime.date(int(date[2]), int(date[0]), int(date[1]))

    try:
        u = User.get(email=current_user_email())

        u.project = request.forms.getunicode('project', None)
        u.office = request.forms.getunicode('office', None)
        u.name = request.forms.getunicode('name', None)
        u.skype = request.forms.getunicode('skype', None)
        u.phone = request.forms.getunicode('phone', None)
        u.title = request.forms.getunicode('title', None)
        birthday = request.forms.getunicode('birthday', None).split("/")
        onboard = request.forms.getunicode('onboard', None).split("/")
        u.birthday = get_date_from(birthday)
        u.onboard = get_date_from(onboard)

        u.completion = True
        u.save()
    except Exception as e:
        logging.error("can't save the user in mongo:" + e)
        return {'status': 'error',
                'message': "failed save user."}

    redirect('/')

@app.route('/upload', method='POST')
def upload():
    upload = request.files.get('file')
    image_url = provider.store(upload.file)
    email = urllib.parse.unquote(request.get_cookie("uid"))
    try:
        current_user = User.get(email=email)
        current_user.raw_image = image_url
        current_user.save()
    except User.DoesNotExist:
        current_user = User.create(raw_image=image_url, name="", title="", birthday="", onboard="", email=email)
    return str(current_user.id)

@app.route("/token")
def token():
    return provider.token()

@app.route("/photo")
@view("edit-photo")
def crop_photo():
    email = current_user_email()
    user  = User.get(email=email)
    return { 'image': user.raw_image + '?imageView/2/w/1200/h/1600' }

@app.route("/avatar")
@view("edit-avatar")
def crop_photo():
    email = current_user_email()
    user  = User.get(email=email)
    return { 'image': user.photo }

@app.route("/profile")
@view("edit-profile")
def crop_photo():
    user  = User.get(email=current_user_email())
    return { "photo": user.photo, 
            "avatar": user.avatar,
            "name": user.name or "",
            "phone": user.phone or "",
            "skype": user.skype or "",
            "project": user.project or "",
            "birthday": user.birthday or "",
            "onboard": user.onboard or "" }


@app.route('/crop', method='POST')
def editPhoto():
    img_src = request.forms.get("src", None)
    x = request.forms.get("x", None)
    y = request.forms.get("y", None)
    width = request.forms.get("w", None)
    height = request.forms.get("h", None)
    img_type = request.forms.get("image_type", None)
    img_width = request.forms.get("image_width", None)
    email = current_user_email()
    try:
        image = crop_image(img_src, img_width, int(round(float(x))), int(round(float(y))), int(round(float(width))), int(round(float(height))))
        image_url = provider.store_file(image)

        user = User.get(email=email)
        if img_type == 'photo':
            user.photo=image_url
        if img_type == 'avatar':
            user.avatar=image_url
        user.save()
    except Exception as e:
        logging.exception("unexpected error {}", e)
        abort(500, "Failed to crop image for user: "+ email)

    return 'Success'


if __name__ == '__main__':
    mimetypes = {"js": 'application/javascript', "css" : "text/css", "images": "image/png"}

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

    debug(True)
    run(app=app, host='0.0.0.0', port=8080, reloader=True)
else:
    application = default_app()

