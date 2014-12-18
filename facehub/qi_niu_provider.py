import logging
from qiniu import Auth, put_file

class QiNiuProvider(object):
    def __init__(self, access_key, secret_key, bucket_name):
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name

    def upload_file(self, file_path, file_name): 
        print(self.access_key)
        print(self.secret_key)
        print(self.bucket_name)
        ret, err = put_file(self.__get_token(file_name), file_name, file_path)
        if err is not None:
            logging.error('error: %s' % err)
        return file_name

    def __get_token(self, file_name):
        q = Auth(self.access_key, self.secret_key)
        return q.upload_token(self.bucket_name, file_name)  
