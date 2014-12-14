import unittest
import sys

from peewee import *
from playhouse.test_utils import test_database

from services.model import User, Project
from services.serializer import Serializer

test_db = SqliteDatabase('facehub.db')

class UserTest(unittest.TestCase):

    def test_serializer(self):
        with test_database(test_db, (User, Project)):
            p = Project.create(name = 'Google Research')
            User.create(name = "Jeff Dean",
                        title = "Technical Follow",
                        email = "jeff@google.com",
                        project = p,
                        avatar = "http://davidx.qiniudn.com/liuliang_head@2x.jpg",
                        photo = "http://davidx.qiniudn.com/liuliang_half@2x.jpg",
                        phone = "13060245883")

            u = User.get(User.name == "Jeff Dean")

            self.assertEqual(u.email, "jeff@google.com")
            self.assertEqual(u.project.name, "Google Research")