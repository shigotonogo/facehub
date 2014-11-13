
class User(object):

	@property
	def name(self):
		return self.__dict__['name']

	@name.setter
	def name(self, value):
		self.__dict__['name']=value

	@property
	def department(self):
		return self.__dict__['department']

	@department.setter
	def department(self, value):
		self.__dict__['department'] = value