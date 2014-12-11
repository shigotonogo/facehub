import logging

from mongokit import Connection
from bottle import Bottle, run, abort, static_file, debug, default_app, request

from utils import jsonify
from model import User, Project
from settings import *


app = Bottle()

connection = Connection(host=MONGO_HOST)
connection.register([User, Project])


@app.route("/api/users", method='GET')
def users(mongodb):
    users = [user.to_json_type() for user in connection.facehub.User.find()]
    return jsonify(users=users)


@app.route('/api/users/<id:int>', method='GET')
def user(mongodb, id):
    user = connection.facehub.User.find_one(id)
    if user is not None:
        return jsonify(user.to_json_type())
    else:
        abort(404, "No such user.")


@app.route('/api/users', method='POST')
def createUser(mongodb):

    project = connection.facehub.Project()
    project['name'] = request.forms.get('project', None)

    user = connection.facehub.User()
    user['name'] = request.forms.get('name', None)
    user['title'] = request.forms.get('title', None)
    user['project'] = project
    user['email'] = request.forms.get('email', None)
    user['skype'] = request.forms.get('skype', None)
    user['photo'] = request.forms.get('phone', None)
    user['phone'] = request.forms.get('phone', None)

    try:
        project.save()
        user.save()
    except Exception as e:
        logging.exception("unexpected error {}", e)
    if not user_id:
        logging.error("can't save the user in mongo")
        return {'status': 'error',
                'message': "failed save user."}
    else:
        return {'status': 'error',
            'message': "the field is not satisfied."}

                'message': "the field is not satisfied."}

if __name__ == '__main__':
    assets = "public/assets/"
    mimetypes = {"js": 'application/javascript', "css" : "text/css", "images": "image/png"}

    @app.route('/')
    def index():
        return static_file("index.html", root="../public/views/", mimetype="text/html")

    @app.route("/assets/<type>/<filename:path>")
    def assets(type, filename):
        return static_file(filename, root="../public/assets/" + type, mimetype=mimetypes[type])

    @app.route('/edit')
    def editPhoto():
        return static_file("edit-photo.html", root="../public/views/", mimetype="text/html")

    debug(True)
    run(app=app, host='0.0.0.0', port=8080, reloader=True)
else:
    application = default_app()

