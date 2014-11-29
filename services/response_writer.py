import json

from bottle import response

def render(content_type="application/json"):
    def response_wrapper(func):
        def wrapper(*args, **kwargs):
            response.content_type = content_type
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                result = dict(status='error',
                              reason=str(e))
            return json.dumps(result)
        return wrapper
    return response_wrapper
