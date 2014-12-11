import unittest
import sys

from mongokit import Connection

from services.model import User, Project

connection = Connection()
connection.register([User, Project])

class UserTest(unittest.TestCase):

    @unittest.skip("testing skipping")
    def tearDown(self):
        connection.test.drop_collection("projects")
        connection.test.drop_collection("users")

    @unittest.skip("testing skipping")
    def test_creation(self):
        project = connection.test.Project()
        project['name'] = "rea myfun"
        project.save()

        user = connection.test.User()
        user['name'] = u'Michael'
        user['title'] = u'Product Manager'
        user['project'] = project
        user['email'] = u'michael@rea-group.com'
        user.save()

        saved_user = connection.test.User.find_one({'name': u'Michael'})
        self.assertEqual(saved_user['name'], u'Michael')
        self.assertEqual(saved_user['project']['name'], u'rea myfun')
