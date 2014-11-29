
class BaseService(object):
    def __init__(self, mongodb):
        self.mongodb = mongodb


class UserService(BaseService):
    def find_by_name(self, name):
        return self.user_col.find_one({'name': name})

    def find_by_id(self, id):
        return self.mongodb['users'].find({'id' : id})

    def save(self, user):
        user['id'] = self.mongodb['users'].count() + 1
        return self.mongodb['users'].save(user)

    def get_all_users(self):
        return self.mongodb['users'].find()
