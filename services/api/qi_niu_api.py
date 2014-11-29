import logging
import os
import qiniu.io
import qiniu.conf
import qiniu.rs
import sys
from facehub.settings import *

class QiNiuAPi:
    qiniu.conf.ACCESS_KEY = QINIU_ACCESS_KEY
    qiniu.conf.SECRET_KEY = QINIU_SECRET_KEY
    bucket_name = PROJECT_NAME

    token=None

    def upload(self, file_path):
        uptoken = self.__get_token()
        file_name = os.path.basename(file_path)
        qiniu.rs.Client().delete(self.bucket_name, file_name)
        localfile = "%s" % file_path
        ret, err = qiniu.io.put_file(uptoken, file_name, localfile)
        if err is not None:
            logging.error('error: %s ' % err)
            return
        else:
            return "http://facehub.qiniudn.com/%s" % file_name

    def __get_token(self):
        policy = qiniu.rs.PutPolicy('facehub')
        return policy.token()   

if __name__ == '__main__':
    QiNiuAPi().upload('./tmp/test.png')







