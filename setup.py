from distutils.core import setup

setup(name='pkgtest',
      version='1.0',
      author='Bryan Thrall',
      author_email='bthrall@velocidata.com',
      url='http://www.example.com',
      packages=['pkgtest'],
      package_data={'pkgtest': ['data/*.dat']},
      )
