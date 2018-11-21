#!/usr/bin/env python

from distutils.core import setup

setup(
    name='Text Frequencies Analysis',
    version='1.0.0',
    author='Elia Mercatanti',
    author_email='emercatanti@gmail.com',
    description='Implement the Hill cipher.',
    long_description=open('README.md').read(),
    license='LICENSE.txt',
    platforms=['Windows', 'MacOS', 'UNIX', 'Linux'],
    requires=['numpy', 'matplotlib', 'pandas']
)
