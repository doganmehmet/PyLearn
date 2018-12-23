try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# config = {
#     'description': 'An Amazingo App',
#     'author': 'Mehmet Dogan',
#     'url': 'mdogan.io',
#     #'download_url': 'GitHub',
#     'author_email': 'm.dogan@mail.com',
#     'version': '0.1',
#     #'install_requires': [''],
#     'packages': ['amazingo'],
#     #'scripts': [],
#     'name': 'amazingo'
# }
#
#
# setup(**config)

setup(name='amazingo',
      version='0.1',
      description='The amazingo joke in the world',
      #url='http://github.com/storborg/funniest',
      author='Mehmet Dogan',
      author_email='m.dogan@mdogan.io',
      license='MIT',
      packages=['amazingo'],
      zip_safe=False)
