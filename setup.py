"""
Setup file for reporty library
"""

from setuptools import setup

DISTNAME = 'boyer'

VERSION = '0.0.1'

DESCRIPTION = "Andrew Boyer's personnal python library"

LONG_DESCRIPTION = """
**boyer** is a python library that contains useful 
functions for Andrew Boyer


Functions:
* Hello

More functions **coming soon**

Report any bugs or email us with questions: andrewsboyer2@gmail.com
"""

LICENSE = 'MIT'

AUTHOR = 'Andrew Boyer'

EMAIL = 'andrewsboyer2@gmail.com'

URL = 'https://github.com/asboyer2/reporty'

KEYWORDS = ['report', 'email', 'plot', 'graph', 'embed']

REQUIREMENTS = ['pyaml']

PYTHON = ">=3.5"

setup(name=DISTNAME,
      packages=['reporty'],
      package_dir={'reporty': 'module/reporty'},
      package_data={'reporty': ['templates/*.yaml']},
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
      include_package_data=True
      )
