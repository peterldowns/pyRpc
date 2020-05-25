#!/usr/bin/env python
# coding: utf-8
from __future__ import print_function
from __future__ import unicode_literals

try:
    from setuptools import setup, find_packages
except ImportError:
    import ez_setup
    ez_setup.use_setuptools()
    from setuptools import setup, find_packages

import os

from pyRpc import __version__

setup(
    name = "pyRpc",
    version = __version__,
    url = 'https://github.com/justinfx/pyRpc',
    packages = find_packages(),
    include_package_data = True,
    install_requires = ['pyzmq'],
    author = "Justin Israel",
    author_email = "justinisrael@gmail.com",
    description = "A simple remote procedure call module using ZeroMQ",
    license = "BSD",
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications',
    ]
)
