import datetime

from mongokit import Document

class Users(Document):
    __collection__ = 'users'

    structure = {
        'name': str,
        'create_at': datetime.datetime,
    }

    required_fields = ['name']

    default_values = {
        'create_at': datetime.datetime.utcnow
    }