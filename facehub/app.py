from bottle import route, run, abort, response, static_file, debug, default_app, request
from decorators import json_response
from users import user_service, user
import logging


users_list = [
    { "id": 1, "name": "Yao Shaobo", "photo":"http://uxhongkong.com/interviews/img/people/thumb-alain-robillard-bastien.jpg", "position": "MD", "project": "REA myfun.com", "email": "zh.li@thoughtworks.com", "phoneNumber": "13060245883", "skype": "david.xie" },
    { "id": 2, "name": "Dong Yuwei", "photo":"http://uxhongkong.com/interviews/img/people/thumb-andrew-mayfield.jpg","position": "MD", "project": "REA myfun.com", "email": "zh.li@thoughtworks.com", "phoneNumber": "13060245883", "skype": "david.xie" },
    { "id": 3, "name": "Dou Yutao", "photo":"http://uxhongkong.com/interviews/img/people/thumb-boon-yew-chew.jpg","position": "MD", "project": "REA myfun.com", "email": "zh.li@thoughtworks.com", "phoneNumber": "13060245883", "skype": "david.xie" },
    { "id": 4, "name": "Liu Liang", "photo":"http://uxhongkong.com/interviews/img/people/thumb-cornelius-rachieru.jpg", "position": "MD", "project": "REA myfun.com", "email": "zh.li@thoughtworks.com", "phoneNumber": "13060245883", "skype": "david.xie" },
    { "id": 1, "name": "Yao Shaobo", "photo":"http://uxhongkong.com/interviews/img/people/thumb-alain-robillard-bastien.jpg","position": "MD", "project": "REA myfun.com", "email": "zh.li@thoughtworks.com", "phoneNumber": "13060245883", "skype": "david.xie" },
    { "id": 2, "name": "Dong Yuwei", "photo":"http://uxhongkong.com/interviews/img/people/thumb-andrew-mayfield.jpg", "position": "MD", "project": "REA myfun.com", "email": "zh.li@thoughtworks.com", "phoneNumber": "13060245883", "skype": "david.xie" },
    { "id": 3, "name": "Dou Yutao", "photo":"http://uxhongkong.com/interviews/img/people/thumb-boon-yew-chew.jpg", "position": "MD", "project": "REA myfun.com", "email": "zh.li@thoughtworks.com", "phoneNumber": "13060245883", "skype": "david.xie" },
    { "id": 4, "name": "Liu Liang", "photo":"http://uxhongkong.com/interviews/img/people/thumb-cornelius-rachieru.jpg", "position": "MD", "project": "REA myfun.com", "email": "zh.li@thoughtworks.com", "phoneNumber": "13060245883", "skype": "david.xie" }
]

data = {
    'users' : users_list
}


@route("/api/users")
@json_response
def users():
    return data

@route('/api/users/<id>')
def user(id):
    for u in users_list:
        if u['id'] == int(id):
            return u
    abort(404, "No such user.")

@route('/api/users', method='POST')
@json_response
def createUser():
    name = request.forms.get('name', None)
    position = request.forms.get('position', None)
    email = request.forms.get('email', None)
    project = request.forms.get('project', None)
    phoneNumber = request.forms.get('phoneNumber', None)
    skype = request.forms.get('skype', None)

    if name is not None and position is not None and project is not None and email is not None:
        user = User()
        user.name = name
        user.position = position
        user.project = project
        user.email = email
        user.phoneNumber = phoneNumber
        user.skype = skype

        try:
            userId = UserService.save(user)
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

    @route('/')
    def index():
        return static_file("index.html", root="public/views/", mimetype="text/html")

    @route("/assets/<type>/<filename:path>")
    def assets(type, filename):
        return static_file(filename, root="public/assets/" + type, mimetype=mimetypes[type])

    debug(True)
    run(host='0.0.0.0', port=8080, reloader=True)
else:
    application = default_app()

