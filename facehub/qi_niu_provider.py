import logging
from qiniu import Auth, put_file
from qiniu import BucketManager

class QiNiuProvider(object):
    def __init__(self, access_key, secret_key, bucket_name):
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name
        self.credentials = Auth(self.access_key, self.secret_key)
    
    def token(self):
        return self.credentials.upload_token(self.bucket_name)


    def upload_file(self, file_path, file_name): 
        upload_token = self.credentials.upload_token(self.bucket_name, file_name)  
        ret, err = put_file(upload_token, file_name, file_path)
        if ret is not None:
            return "http://7rylsb.com1.z0.glb.clouddn.com/%s" % file_name
        else:
            logging.error('upload: %s error.' % file_name)
    def get_stat(self, key):
        bucket = BucketManager(self.credentials)
        ret, info = bucket.stat(self.bucket_name, key)
        
