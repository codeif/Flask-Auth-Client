#!/usr/bin/env python
import os

from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='Flask-Auth-Client',
    version='0.0.3',
    description='API client for flask extension',
    long_description=read('README.rst'),
    author='codeif',
    author_email='me@codeif.com',
    url='https://github.com/codeif/Flask-Auth-Client',
    license='MIT',
    packages=find_packages(),
    install_requires=['Flask', 'requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
    ]
)
