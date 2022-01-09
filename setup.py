# -*- coding: utf-8 -*-
import re
from setuptools import setup
from io import open

VERSION = '0.0.1'

long_description = open('README.md', 'rt', encoding='utf8').read()

# PyPI can't process links with anchors
long_description = re.sub(r'<(.*)#.*>`_', '<\g<1>>`_', long_description)

setup(
    name='client-payment-sdk',
    packages=['client_payment_sdk'],

    description='Client Payment Python SDK',
    long_description=long_description,

    version=VERSION,

    author='SpaceAround101',
    author_email='viksnamax@mail.ru',
    license='MIT license',

    url='https://github.com/Space-Around/client-payment-sdk-python.git',
    download_url='https://github.com/Space-Around/client-payment-sdk-python.git/tarball/%s' % VERSION,

    requires=[
        'requests (>=2.9.1)',
        'jwcrypto (>=1.0)',
        'setuptools (>=57.0.0)'
    ],

    install_requires=[
        'requests >=2.9.1',
        'jwcrypto >=1.0',
        'setuptools >=57.0.0'
    ],

    classifiers=[
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Office/Business',
        'Topic :: Office/Business :: Financial',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],

    zip_safe=False
)
