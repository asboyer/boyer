from setuptools import setup

DISTNAME = 'boyer'

VERSION = '0.1.6'

DESCRIPTION = "Andrew Boyer's personal python library"

LONG_DESCRIPTION = """
**boyer** is a python library that contains useful 
functions for Andrew Boyer

Available functions:
* Hello
* Delay Print
* Clear
* Memify
* Clean
* Encrypt
* Decrypt
* Capitalize
* Get Num

Report any bugs or email us with questions: asboyer@gmail.com
"""

LICENSE = 'MIT'

AUTHOR = "Andrew Boyer"

EMAIL = 'asboyer@gmail.com'

URL = 'https://github.com/asboyer/boyer'

KEYWORDS = ['boyer']

REQUIREMENTS = []

PYTHON = ">=3.5"

setup(name=DISTNAME,
      packages=['boyer'],
      package_dir={'boyer': 'module/boyer'},
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type='text/markdown',
      license=LICENSE,
      author=AUTHOR,
      author_email=EMAIL,
      url=URL,
      keywords=KEYWORDS,
      install_requires=REQUIREMENTS,
      python_requires=PYTHON,
      )
