import os
import hashlib
from qi_niu_provider import QiNiuProvider

class Provider(object):
    def __init__(self, api):
        self.api = api

    def put_file(self, file_path):
        name, extension = os.path.splitext(file_path)
        return self.api.upload_file(file_path, self.__md5_name(name) + extension)

    def __md5_name(self, name):
        return hashlib.md5(name.encode('utf8')).hexdigest()

def get_one(access_key, secret_key, bucket_name=None):
    api =  QiNiuProvider(access_key, secret_key, bucket_name)
    return Provider(api)

