#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup, find_packages


PROJECT_NAME = os.path.basename(os.path.abspath(os.curdir))

PROD_PACKAGES = [
    'backoff>=1.8.0',
    'docker-compose<=1.24.0', # See conflict issues below
    'lovely-pytest-docker<=0.0.5',
    'pg8000>=1.13.2',
    'pytest>=3.5.0',
    'requests<2.21', # Throttled by docker-compose 1.24.0
    'urllib3<1.25,>=1.21.1', # Throttled by requests 2.20.1 from docker-compose (conflict with botocore>=1.12.164)
]

DEV_PACKAGES = [
    'pylint',
    'sphinx_rtd_theme',
    'twine',
    'Sphinx',
]

PACKAGES = list(PROD_PACKAGES)
if (os.environ.get('APP_ENV') is not None and
        'dev' in os.environ.get('APP_ENV')):
    PACKAGES += DEV_PACKAGES


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-docker-postgresql',
    version='0.1.0',
    author='Lou Markovski',
    author_email='lou.markovski@gmail.com',
    maintainer='Lou Markovski',
    maintainer_email='lou.markovski@gmail.com',
    license='MIT',
    url='https://github.com/loum/pytest-docker-postgresql',
    description='A simple plugin to use with pytest',
    long_description=read('README.rst'),
    py_modules=['pytest_docker_postgresql'],
    python_requires='>=3.6',
    install_requires=PACKAGES,
    packages=find_packages() + ['pytest_docker_postgresql'],
    package_data={'pytest_docker_postgresql/docker': ['*.yml', '.env']},
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'postgresql = pytest_docker_postgresql',
        ],
    },
)
