#!/usr/bin/env python
import os
from setuptools import setup
from setuptools import find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='maji',
    version='0.1.0',
    author='Amirouche Boubekki',
    author_email='amirouche@hypermove.net',
    url='https://github.com/amirouche/maji',
    description='very simple markdown + jinja2 static site generator',
    long_description=read('README.rst'),
    py_modules=['maji'],
    zip_safe=False,
    license='GPLv3+',
    entry_points="""
    [console_scripts]
    maji=maji:main
    """,
    install_requires=[
        'daiquiri',
        'docopt',
        'jinja2',
        'lxml',
        'mistune',
        'pygments',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        'Programming Language :: Python :: 3',
    ],
)
