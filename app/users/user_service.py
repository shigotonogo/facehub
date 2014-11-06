from pymongo import MongoClient
import datetime

class UserService:
	def __init__(self):
		self.client = MongoClient()
		self.db = self.client.facehub
		self.user_col = self.db.users

	def find_by_name(self, name):
		return self.user_col.find_one({'name': name})

	def save(self, user):
		return self.user_col.save(user.__dict__)
