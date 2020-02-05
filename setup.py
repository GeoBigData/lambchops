import sys
import os.path
from setuptools import setup, find_packages

open_kwds = {}
if sys.version_info > (3,):
    open_kwds['encoding'] = 'utf-8'

here = os.path.abspath(os.path.dirname(__file__))

req_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "requirements.txt")
with open(req_path, **open_kwds) as f:
    requires = f.read().splitlines()

setup(
      name='lambchops',
      version='0.0.5',
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
