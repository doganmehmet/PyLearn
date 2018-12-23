# A Project Skeleton

# This will be where you start learning how to set up a good project ”skeleton” directory. This skeleton
# directory will have all the basics you need to get a new project up and running. It will have your project
# layout, automated tests, modules, and install scripts. When you go to make a new project, just copy this
# directory to a new name and edit the files to get started.


# pip3 install virtualenv
# whereis virtualenv
# virtualenv myproject
# source myproject/bin/activate  or . myproject/bin/activate - to activate
# deactivate - to deactivate
# which python - it shows where it runs the python from
# pip install nose


# Keep your virtual environments separate from your projects

# Projects
    # contain your source code
    # under version control

# Virtual environments
    # contain libraries, tools, python interpreter etc.
    # keep them in a directory like ~/ .virtualenvs


# Creating the Skeleton Project Directory

# mkdir skeleton
# cd skeleton
# mkdir bin NAME tests docs
# touch NAME/__init__.py
# touch tests/__init__.py
# create setup.py file in skeleton directory
# the setup.py details
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'My Name',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)


# tests/NAME_tests.py
# the NAME_tests.py details
from nose.tools import *
import NAME

def setup():
    print("SETUP")

def teardown():
    print("TEAR DOWN!")

def test_basic():
    print("I RAN", end = '')

# nosetests - we should run it in skeleton directory not in tests directory
