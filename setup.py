"""
Setup file for the afsapi package
"""
from setuptools import setup, find_packages

PACKAGES = find_packages(exclude=['tests', 'tests.*'])

REQUIRES = [
    'aiohttp>=1.3.1',
    'lxml>=3.6.0'
]

PROJECT_CLASSIFIERS = [
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.0',
    'Programming Language :: Python :: 3.1',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Topic :: Software Development :: Libraries'
]

setup(name='afsapi',
      version='0.0.2',
      description='Asynchronous Implementation of the Frontier Silicon API',
      author='Krasimir Zhelev',
      author_email='krasimir.zhelev@gmail.com',
      keywords='afsapi async fsapi frontier silicon',
      license="Apache License 2.0",
      download_url='https://github.com/zhelev/python-afsapi/archive/0.0.1.zip',
      url='https://github.com/zhelev/python-afsapi.git',
      maintainer='Krasimir Zhelev',
      maintainer_email='krasimir.zhelev@gmail.com',
      zip_safe=True,
      include_package_data=True,
      packages=PACKAGES,
      platforms='any',
      install_requires=REQUIRES,
      classifiers=PROJECT_CLASSIFIERS,
     )
