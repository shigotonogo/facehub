import os
import uuid
import logging

from qiniu import Auth, put_file, put_data, BucketManager

from utils import hash

def provider(access_key, secret_key, bucket_name, image_server_url):
    api =  QiNiuProvider(access_key, secret_key, bucket_name, image_server_url)
    return Storage(api)


class Storage(object):
    def __init__(self, api):
        self.api = api

    def store_file(self, file_path):
        name, extension = os.path.splitext(file_path)
        return self.api.store_file(file_path, hash(name) + extension)

    def store(self, raw):
        return self.api.store(raw)

    def token(self):
        return self.api.token()


class QiNiuProvider(object):

    def __init__(self, access_key, secret_key, bucket_name, imageServerUrl):
        self.access_key = access_key
        self.secret_key = secret_key
        self.bucket_name = bucket_name
        self.imageServerUrl = imageServerUrl
        self.credentials = Auth(self.access_key, self.secret_key)

    def token(self):
        return self.credentials.upload_token(self.bucket_name)

    def store(self, raw):
        key = hash(str(uuid.uuid1()))
        upload_token = self.credentials.upload_token(self.bucket_name, key)
        ret, err = put_data(upload_token, key, raw)
        if ret is not None:
            return "%s/%s" % (self.imageServerUrl, ret['key'])
        else:
            logging.error('upload error.')


    def store_file(self, file_path, file_name):
        upload_token = self.credentials.upload_token(self.bucket_name, file_name)
        ret, err = put_file(upload_token, file_name, file_path)
        if ret is not None:
            return "%s/%s" % (self.imageServerUrl, ret['key'])
        else:
            logging.error('upload: %s error.' % file_name)
