import logging
import json
from bson.json_util import dumps

from bottle import Bottle, run, abort, static_file, debug, default_app, request
from bottle.ext.mongo import MongoPlugin

from utils import jsonify
from users.user_service import UserService
from users.user import User
from settings import *


app = Bottle()
plugin = MongoPlugin(uri=MONGO_HOST, db=MONGO_DATABASE, json_mongo=True)
app.install(plugin)


@app.route("/api/users", method='GET')
def users(mongodb):
    user_service = UserService(mongodb)
    users = json.loads(dumps(user_service.get_all_users()))
    return jsonify(users=users)


@app.route('/api/users/<id:int>', method='GET')
def user(mongodb, id):
    user_service = UserService(mongodb)
    users = user_service.find_by_id(id)
    if users.count():
        user = json.loads(dumps(users))[0]
        return jsonify(user)
    else:
        abort(404, "No such user.")


@app.route('/api/users', method='POST')
def createUser():
    name = request.forms.get('name', None)
    position = request.forms.get('position', None)
    email = request.forms.get('email', None)
    project = request.forms.get('project', None)
    phoneNumber = request.forms.get('phoneNumber', None)
    skype = request.forms.get('skype', None)

    if name is not None and position is not None and project is not None and email is not None:
        user = User(name)
        user.position = position
        user.project = project
        user.email = email
        user.phoneNumber = phoneNumber
        user.skype = skype

        userId = None
        try:
            user_service = UserService()
            userId = user_service.save(user)
        except Exception as e:
            logging.exception("unexpected error {}", e)
        if not userId:
            logging.error("can't save the user in mongo")
            return {'status': 'error',
                    'message': "failed save user."}
    else:
        return {'status': 'error',
                'message': "the field is not satisfied."}

if __name__ == '__main__':
    assets = "public/assets/"
    mimetypes = {"js": 'application/javascript', "css" : "text/css", "images": "image/png"}

    @app.route('/')
    def index():
        return static_file("index.html", root="public/views/", mimetype="text/html")

    @app.route("/assets/<type>/<filename:path>")
    def assets(type, filename):
        return static_file(filename, root="public/assets/" + type, mimetype=mimetypes[type])

    debug(True)
    run(app=app, host='0.0.0.0', port=8080, reloader=True)
else:
    application = default_app()

