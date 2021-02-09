from setuptools import setup

DISTNAME = 'boyer'

VERSION = '0.0.5'

DESCRIPTION = "Andrew Boyer's personnal python library"

LONG_DESCRIPTION = """
**boyer** is a python library that contains useful 
functions for Andrew Boyer

Functions:
* Hello
* Delay Print

Get int is **coming soon**

Report any bugs or email us with questions: andrewsboyer2@gmail.com
"""

LICENSE = 'MIT'

AUTHOR = "Andrew Boyer"

EMAIL = 'andrewsboyer@gmail.com'

URL = 'https://github.com/asboyer2/boyer'

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
