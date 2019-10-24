import sys
import os.path
from setuptools import setup, find_packages
import configparser

open_kwds = {}
if sys.version_info > (3,):
    open_kwds['encoding'] = 'utf-8'

here = os.path.abspath(os.path.dirname(__file__))

req_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "requirements.txt")
with open(req_path, **open_kwds) as f:
    requires = f.read().splitlines()

# Get the version from the package
config = configparser.ConfigParser()
config.read(os.path.join(here, '.bumpversion.cfg'))
version = config['bumpversion']['current_version']

# with open('README.md', **open_kwds) as f:
#     readme = f.read()

# long_description=readme,

setup(
      name='lambchops',
      version=version,
      python_requires='>=3.6',
      description='CLI tools for compiling AWS Lambda functions and layers',
      classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'Operating System :: MacOS :: MacOS X',
            'Programming Language :: Python',
      ],
      keywords='',
      author='Maxar',
      author_email='jon.duckworth@maxar.com',
      url='',
      license='MIT',
      packages=find_packages(exclude=['examples', 'env']),
      package_data={
            'lambchops':  ['compilers/*']
      },
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      entry_points={
            'console_scripts': [
                  'lambchops = lambchops.lambchops:lambchops',
            ]
      }
)
