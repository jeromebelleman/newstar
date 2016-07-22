#!/usr/bin/env python
# coding=utf-8

import os
from distutils.core import setup

delattr(os, 'link')

setup(
    name='newstar',
    version='1.3-2',
    author='Jerome Belleman',
    author_email='Jerome.Belleman@gmail.com',
    url='http://cern.ch/jbl',
    description="Nova shell",
    long_description="Cross-tenant Nova shell to perform mass operations.",
    scripts=['newstar'],
    data_files=[('share/man/man1', ['newstar.1'])],
)
