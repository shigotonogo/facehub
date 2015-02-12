import logging
from json import dumps
from bottle import *
from model import *
from serializer import Serializer
import storage
from image import crop_image

from playhouse.db_url import connect

app = Bottle()
TEMPLATE_PATH.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), './templates')))
app.config.load_config('facehub.cfg')

db = connect(app.config['database.url'])
initDatabase(db)
ser = Serializer()
provider = storage.provider(app.config['cloud.accesskey'], app.config['cloud.secretkey'],app.config['cloud.bucket'])

@app.route("/api/users", method='GET')
def users():
    response.content_type = 'application/json'
    resp = {"users": [ser.serialize_object(u, fields={Project: ['name']}) for u in User.select()]}
    return dumps(resp)

@app.route('/api/users/<id:int>', method='GET')
def user(id):
    response.content_type = 'application/json'
    user = User.get(User.id == id)
    if user is not None:
        return dumps(ser.serialize_object(user, fields={Project: ['name']}))
    else:
        abort(404, "No such user.")

@app.route('/api/users', method='POST')
def createUser():
    try:
        u = User.get(id=request.forms.get('user_id', None))

        p = Project(name=request.forms.get('project', None))
        u.project = p
        u.name = request.forms.get('name', None)
        u.email = request.forms.get('email', None)
        u.skype = request.forms.get('skype', None)
        u.phone_number = request.forms.get('phone', None)
        u.title = request.forms.get('title', None)

        p.save()
        u.save()
    except Exception as e:
        logging.exception("unexpected error {}", e)

    if not u.id:
        logging.error("can't save the user in mongo")
        return {'status': 'error',
                'message': "failed save user."}
    redirect('/')

@app.route('/upload', method='POST')
def upload():
    upload = request.files.get('file')
    image_url = provider.store(upload.file)
    new_user = User.create(raw_image=image_url, name="", title="", email="")
    return str(new_user.id)

@app.route("/token")
def token():
    return provider.token()

@app.route("/users/<user_id>/photo/crop")
@view("edit-photo")
def crop_photo(user_id):
    user  = User.get(id=user_id)
    return { 'id': user_id, 'image': user.raw_image }

@app.route("/users/<user_id>/avatar/crop")
@view("edit-avatar")
def crop_photo(user_id):
    user  = User.get(id=user_id)
    return { 'id': user_id, 'image': user.photo }

@app.route("/users/<user_id>/profile")
@view("edit-profile")
def crop_photo(user_id):
    user  = User.get(id=user_id)
    return { 'id': user_id, 'photo': user.photo, 'avatar': user.avatar }


@app.route('/crop', method='POST')
def editPhoto():
    user_id = request.forms.get("user_id")
    img_src = request.forms.get("src", None)
    x = request.forms.get("x", None)
    y = request.forms.get("y", None)
    width = request.forms.get("w", None)
    height = request.forms.get("h", None)
    img_type = request.forms.get("image_type", None)

    try:
        image = crop_image(img_src, int(round(float(x))), int(round(float(y))), int(round(float(width))), int(round(float(height))))
        image_url = provider.store_file(image)

        user = User.get(id=user_id)
        if img_type == 'photo':
            user.photo=image_url
        if img_type == 'avatar':
            user.avatar=image_url
        user.save()
    except Exception as e:
        logging.exception("unexpected error {}", e)
        abort(500, "Failed to crop image for user: "+ user_id)

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

