
class User(object):
	def __init__(self, name):
		self.name = name
	
	def __set__(self, k, v):
		self.__dict__[k] = v
