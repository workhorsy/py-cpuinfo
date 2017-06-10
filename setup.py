# Copyright (c) 2014-2017, Matthew Brennan Jones <matthew.brennan.jones@gmail.com>
# Py-cpuinfo is a Python module to show the cpuinfo of a processor
# It uses a MIT style license
# It is hosted at: https://github.com/workhorsy/py-cpuinfo

import os
from setuptools import setup

with open(os.path.join(os.getcwd(), 'README.rst'), 'r') as f:
    readme_content = f.read()

setup(
    name = "py-cpuinfo",
    version = "3.3.0",
    author = "Matthew Brennan Jones",
    author_email = "matthew.brennan.jones@gmail.com",
    description = "Get CPU info with pure Python 2 & 3",
    long_description=readme_content,
    license = "MIT",
    url = "https://github.com/workhorsy/py-cpuinfo",
    packages=['cpuinfo'],
    test_suite="test_suite",
    entry_points = {
        'console_scripts': ['cpuinfo = cpuinfo:main'],
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ],
)
