import datetime

from mongokit import Document, Connection

class Users(Document):

    structure = {
        'name': str,
        'create_at': datetime.datetime,
    }

    required_fields = ['name']

    default_values = {
        'create_at': datetime.datetime.utcnow
    }