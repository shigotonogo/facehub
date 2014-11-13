import json
from bottle import response


def json_response(func):
    def wrapper(*args, **kwargs):
        response.content_type = 'application/json'
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            result = dict(status='error',
                          reason=str(e))
        return json.dumps(result)
    return wrapper
