from bottle import route, run, abort, response, static_file, debug, default_app
from decorators import json_response


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
    run(host='localhost', port=8080, reloader=True)
else:
    application = default_app()

