import unittest

from mongokit import Connection

from services.user import Users

connection = Connection()
connection.register([Users])

class UserTest(unittest.TestCase):

    def test_creation(self):
        model = connection.test.user.Users()
        model['name'] = u'facehub'
        model.save()

        persisted = connection.test.user.Users.find_one({'name': u'facehub'})
        self.assertEqual(persisted['name'], u'facehub')
