import datetime
import json

from peewee import *

db_proxy = Proxy()

def initDatabase(db):
    db_proxy.initialize(db)

class BaseModel(Model):

    class Meta:
        database = db_proxy

class Project(BaseModel):
    id = PrimaryKeyField()
    name = CharField(index=True)
    description =  TextField(null=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)

class User(BaseModel):
    id = PrimaryKeyField()
    project = ForeignKeyField(Project, related_name='project', null=True)
    name = CharField(index=True)
    title = CharField(null=False)
    email = CharField(null=False)
    avatar = CharField()
    photo = CharField()
    phone = CharField(null=True)
    skype = CharField(null=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    updated_at = DateTimeField(default=datetime.datetime.now)