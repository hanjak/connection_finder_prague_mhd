from setuptools import setup



def get_install_requires():
    with open('requirements.txt') as f:
        return [req.strip() for req in f]

def get_long_description():
    with open('README.md') as f:
        long_description = f.read()

REQUIREMENTS = ['requests']

setup(name='myraptor',
      version='1.0.0',
      description='Prague public transport connection finder using RAPTOR algorithm',
      long_description=get_long_description(),
      url='https://github.com/hanjak/connection_finder_prague_mhd',
      author='Hana Kosova',
      author_email='hanja.kosova@gmail.com',
      license='MIT',
      packages=['myraptor'],
      install_requires=get_install_requires(),
      keywords='raptor connection finder'
      )