import datetime
import json

from peewee import *

db_proxy = Proxy()

def initDatabase(db):
    db_proxy.initialize(db)

class BaseModel(Model):

    class Meta:
        database = db_proxy

class User(BaseModel):
    id = PrimaryKeyField()
    project = CharField(null=True)
    name = CharField(index=True)
    title = CharField()
    email = CharField()
    raw_image = CharField(null=True)
    avatar = CharField(null=True)
    photo = CharField(null=True)
    phone = CharField(null=True)
    skype = CharField(null=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        db_table = 'users'