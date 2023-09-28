#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()

def replace_version(version):
    with open('./pytest_steep/__init__.py', 'r') as fi:
        code = fi.read()
    with open('./pytest_steep/__init__.py', 'w') as fo:
        fo.write(code.replace("__version__ = 'dev'", f"__version__ = '{version}'"))


version = os.environ.get('CI_STEEP_RELEASE_VERSION', '0.0.1')
replace_version(version)

from setuptools import find_packages

setup(
    name='pytest_steep',
    version=version,
    author='Clemens Löbner',
    author_email='mikamove@posteo.de',
    maintainer='Clemens Löbner',
    maintainer_email='mikamove@posteo.de',
    license='MIT',
    url='https://github.com/mikamove/pytest-steep',
    description='runs tests in an order such that coverage increases as fast as possible',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    py_modules=['pytest_steep'],
    python_requires='>=3.8',
    install_requires=[
        'pytest>=7.3.1',
        'pytest-donde>=1.0.0',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'steep = pytest_steep.plugin',
        ],
    },
    packages=find_packages(where='.'),
    package_dir={'': '.'}
)
