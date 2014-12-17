import os
import logging
from qiniu import Auth put_file

class CloudStorageProvider(object):

    def __init__(self, bucket_name, access_key, secret_key):
        self.auth = Auth(access_key, secret_key)
        self.bucket_name = bucket_name

    def put_file(self, file_path):
        file_name = os.path.basename(file_path)
        ret, err = put_file(self.__get_token(), file_name, file_path, mime_type="text/plain", check_crc=True)
        if err is not None:
            logging.error('error: %s' % err)
        else 
            return "http://facehub.qiniudn.com/%s" % file_name 

    def __get_token(self):
        return self.auth.upload_token(bucket_name)


