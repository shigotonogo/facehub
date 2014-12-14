import json

from services.model import *

from bottle import ConfigDict
from peewee import MySQLDatabase

cfg = ConfigDict()
cfg.load_config("facehub.cfg")

db = MySQLDatabase(cfg['mysql.db'], host=cfg['mysql.host'], user=cfg['mysql.user'])
initDatabase(db)

tables = db.get_tables()
print(tables)

if 'project' in tables:
    db.drop_tables([Project])
    db.create_tables([Project])
else:
    db.create_tables([Project])


if 'user' in tables:
    db.drop_tables([User])
    db.create_tables([User])
else:
    db.create_tables([User])



with open('tests/fixtures/projects.json', 'r') as f:
    projects = json.loads(f.read())

Project.insert_many(projects).execute()

with open('tests/fixtures/users.json', 'r') as f:
    users = json.loads(f.read())

User.insert_many(users).execute()

User.update(project=Project.get()).execute()
