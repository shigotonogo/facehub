from setuptools import setup, find_packages

import facehub

reqs = [
      "bottle",
      "qiniu"
]

setup(
      name = facehub.__name__,
      version = facehub.__version__,
      packages = find_packages(),
      requires = reqs,
      install_requires = reqs,
      author = facehub.__author__,
      author_email = "myfun.xian@gmail.com",
      description = "Facehub.",
      long_description = "Facehub.",
      license = "Proprietary",
      keywords = "content, CMS",
      url = "http://github.com/shigotonogo/facehub",
      entry_points = {
        'console_scripts': []
      }
)
