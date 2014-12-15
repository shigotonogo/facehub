import logging
from json import dumps

from bottle import *

from model import *
from serializer import Serializer


app = Bottle()
app.config.load_config('facehub.cfg')

db = MySQLDatabase(app.config['mysql.db'], host=app.config['mysql.host'], user=app.config['mysql.user'], password=app.config['mysql.password'])
initDatabase(db)

ser = Serializer()

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
    projet = request.forms.get('project', None)
    name = request.forms.get('name', None)
    title = request.forms.get('title', None)
    project = project
    email = request.forms.get('email', None)
    skype = request.forms.get('skype', None)
    phone_number = request.forms.get('phone', None)
    photo = request.forms.get('photo', None)

    try:
        p = Project(name=project)
        u = User(name=name, title=title, project=p, email=email, skype=skype, phone=phone, photo=photo)
        p.save()
        u.save()
    except Exception as e:
        logging.exception("unexpected error {}", e)
    if not user_id:
        logging.error("can't save the user in mongo")
        return {'status': 'error',
                'message': "failed save user."}
    else:
        return {'status': 'error',
            'message': "the field is not satisfied."}

if __name__ == '__main__':
    mimetypes = {"js": 'application/javascript', "css" : "text/css", "images": "image/png"}

    @app.route('/')
    def index():
        return static_file("index.html", root="facehub/templates/", mimetype="text/html")


    @app.route('/new', method='GET')
    def new():
        return static_file("new.html", root="../public/views/", mimetype="text/html")

    @app.route("/assets/<type>/<filename:path>")
    def assets(type, filename):
        return static_file(filename, root="facehub/static/" + type, mimetype=mimetypes[type])

    @app.route('/edit')
    def editPhoto():
        return static_file("edit-photo.html", root="facehub/templates/", mimetype="text/html")

    debug(True)
    run(app=app, host='0.0.0.0', port=8080, reloader=True)
else:
    application = default_app()

