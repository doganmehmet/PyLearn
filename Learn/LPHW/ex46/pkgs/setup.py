try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup




setup(name='pkgs',
      version='0.1',
      description='The amazing joke in the world',
      #url='http://github.com/storborg/funniest',
      author='Mehmet Dogan',
      author_email='m.dogan@mdogan.io',
      license='MIT',
      packages=['pkgs'],
      zip_safe=False)
