#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'redis'
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

dependency_links = [
    'https://github.com/andymccurdy/redis-py/archive/master.zip#egg=redis'
]

setup(
    name='geo_python',
    version='0.1.2',
    description="Simple GEO library based on Redis GEO function",
    long_description=readme + '\n\n' + history,
    author="Jerry Lau",
    author_email='whilgeek@gmail.com',
    url='https://github.com/jerryleooo/geo_python',
    packages=[
        'geo_python',
    ],
    package_dir={'geo_python':
                 'geo_python'},
    dependency_links=dependency_links,
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='geo_python',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
