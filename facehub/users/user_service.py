
class BaseService(object):
    def __init__(self, mongodb):
        self.mongodb = mongodb


class UserService(BaseService):
    def find_by_name(self, name):
        return self.user_col.find_one({'name': name})

    def save(self, user):
        return self.user_col.save(user.__dict__)

    def get_all_users(self):
        return self.mongodb['users'].find()
