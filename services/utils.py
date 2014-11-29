from json import dumps
from bottle import response

def jsonify(*args, **kwargs):
    response.content_type = 'application/json'
    return dumps(dict(*args, **kwargs))
