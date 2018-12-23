try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Learning ex47 from LPHW',
    'author': 'Mehmet Dogan',
    'url': 'mdogan.io',
    'download_url': 'GitHub',
    'author_email': 'm.dogan@mail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'skeleton'
}

setup(**config)
