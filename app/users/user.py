from base import Base

class User(Base):

	def __init__(self):
		self.values={}

	def __values__(self):
		return self.values

	def set_name(self, name):
		self.values['name']=name

	def get_name(self):
		return self.values['name']

	def set_image(self, image):
		self.values['image']=image

	def get_image(self):
		return self.values['image']