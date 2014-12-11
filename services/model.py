import datetime
import uuid

from mongokit import Document

class Project(Document):
    __collection__ = "projects"

    structure = {
        '_id': str,
        'name': str,
        'description': str,
        'create_at': datetime.datetime,
        'updated_at': datetime.datetime
    }

    required_fields = ['name']

    indexes = [
        {
            'fields': ['name'],
            'unique': True
        }
    ]

    default_values = {
        '_id': str(uuid.uuid4()),
        'create_at': datetime.datetime.utcnow
    }


    def save(self, uuid=False, validate=None, safe=True, *args, **kwargs):
        self['updated_at'] = datetime.datetime.utcnow()
        super(Project, self).save(uuid, validate, safe, *args, **kwargs)

class User(Document):
    __collection__ = 'users'

    structure = {
        '_id': str,
        'name': str,
        'avatar': str,
        'photo' : str,
        'title': str,
        'project': Project,
        'email': str,
        'phone_number': str,
        'skype':str,
        'create_at': datetime.datetime,
        'updated_at': datetime.datetime
    }
    use_autorefs = True

    required_fields = ['name', 'title', 'project', 'email']

    default_values = {
        '_id': str(uuid.uuid4()),
        'create_at': datetime.datetime.utcnow
    }

    def save(self, uuid=False, validate=None, safe=True, *args, **kwargs):
        self['updated_at'] = datetime.datetime.utcnow()
        super(User, self).save(uuid, validate, safe, *args, **kwargs)

