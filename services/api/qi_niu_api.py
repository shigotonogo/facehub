import logging
import os
from qiniu import Auth
from qiniu import put_file
import sys

class QiNiuAPi:
    bucket_name = 'facehub'
    mime_type = 'image/jpeg'

    client = Auth('p0XvMhHCUOwTAUmdJdRvYVL58Set1kIEWQZDk5rF', 'PhFzLVRNFawZc9eM4fUPPyRlSTclientWkALmgxRvegkL')

    def upload(self, file_path):
        key = os.path.basename(file_path)
        token = self.client.upload_token(self.bucket_name, key)
        ret, info = put_file(token, key, file_path)

        print(ret)
        print(info)

if __name__ == '__main__':
    QiNiuAPi().upload('/tmp/testimg.jpg')