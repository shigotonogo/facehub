# import logging
# import os
# import qiniu.io
# import qiniu.conf
# import qiniu.rs
# import sys
# from facehub.settings import *

# class QiNiuAP:

#     token=None

#     def __init__(self, bucket):
#         self.bucket = bucket

#     def upload(self, file_path):
#         uptoken = self.__get_token()
#         file_name = os.path.basename(file_path)
#         qiniu.rs.Client().delete(self.bucket, file_name)
#         localfile = "%s" % file_path
#         ret, err = qiniu.io.put_file(uptoken, file_name, localfile)
#         if err is not None:
#             logging.error('error: %s ' % err)
#             return
#         else:
#             return "http://facehub.qiniudn.com/%s" % file_name

#     def __get_token(self):
#         policy = qiniu.rs.PutPolicy('facehub')
#         return policy.token()

# if __name__ == '__main__':
#     QiNiuAPi("facehub").upload('./tmp/test.png')







