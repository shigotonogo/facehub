from setuptools import setup, find_packages

import services

reqs = [
      "bottle",
      #"bottle-mongo",
      "qiniu"
]

setup(
      name = services.__name__,
      version = services.__version__,
      packages = find_packages(),
      requires = reqs,
      install_requires = reqs,
      author = services.__author__,
      author_email = "he.fei@rea-group.com",
      description = "Facehub.",
      long_description = "Facehub.",
      license = "Proprietary",
      keywords = "content, CMS",
      url = "http://github.com/shigotonogo/facehub",
      entry_points = {
        'console_scripts': []
      }
)
