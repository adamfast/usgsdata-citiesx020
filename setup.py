#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='usgsdata-citiesx020',
    version='1.0.0',
    description='Models and load scripts used to import the U.S. National Atlas Cities and Towns of the United States',
    author='Adam Fast',
    author_email='adamfast@gmail.com',
    url='https://github.com/adamfast/usgsdata-citiesx020',
    packages=find_packages(),
    package_data={
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities'
    ],
)
