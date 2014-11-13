
class User(object):

	@property
	def name(self):
		return self.__dict__['name']

	@name.setter
	def name(self, value):
		self.__dict__['name']=value

	@property
	def position(self):
		return self.__dict__['position']

	@position.setter
	def position(self, value):
		self.__dict__['position'] = value

	@property
	def project(self):
	    return self.__dict__['project']

	@project.setter
	def project(self, value):
	    self.__dict__['project'] = value

	@property
	def email(self):
	    return self.__dict__['email']
	@email.setter
	def email(self, value):
	    self.__dict__['email'] = value

	@property
	def phoneNumber(self):
	    return self.__dict__['phoneNumber']
	@phoneNumber.setter
	def phoneNumber(self, value):
	    self.__dict__['phoneNumber'] = value

	@property
	def skype(self):
	    return self.__dict__['skype']
	@skype.setter
	def skype(self, value):
	    self.__dict__['skype'] = value
	
	
	
	