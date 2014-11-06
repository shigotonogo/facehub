from bottle import route, run, response
from json import dumps

response.content_type = 'application/json'

users = [
            { "id": 1, "name": "Yao Shaobo", "photo":"http://uxhongkong.com/interviews/img/people/thumb-alain-robillard-bastien.jpg" },
            { "id": 2, "name": "Dong Yuwei", "photo":"http://uxhongkong.com/interviews/img/people/thumb-andrew-mayfield.jpg" },
            { "id": 3, "name": "Dou Yutao", "photo":"http://uxhongkong.com/interviews/img/people/thumb-boon-yew-chew.jpg" },
            { "id": 4, "name": "Liu Liang", "photo":"http://uxhongkong.com/interviews/img/people/thumb-cornelius-rachieru.jpg" }
]


@route('/')
def index():
    return dumps(users)


@route('/users/<id>')
def user(id):
    for u in users:
        if u['id'] == id:
            return dumps(u)
    return dumps({})



run(host='localhost', port=8080, debug=True)

