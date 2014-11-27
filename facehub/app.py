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
plugin = MongoPlugin(uri=MONGO_HOST, db=PROJECT_NAME, json_mongo=True)
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
def createUser(mongodb):
    name = request.forms.get('name', None)
    position = request.forms.get('position', None)
    email = request.forms.get('email', None)
    project = request.forms.get('project', None)
    phone = request.forms.get('phone', None)
    skype = request.forms.get('skype', None)
    photo = request.forms.get('photo', None)

    if name and position and project and email:
        user = dict(name=name,
                    position=position,
                    project=project,
                    email=email,
                    phoneNumber=phone,
                    skype=skype,
                    photo=photo)

        user_id = None
        try:
            user_service = UserService(mongodb)
            user_id = user_service.save(user)
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

