

import os
from setuptools import setup


with open(os.path.join(os.getcwd(), 'README.rst'), 'r') as f:
    readme_content = f.read()

setup(
    name = "py-cpuinfo",
    version = "0.1.1",
    author = "Matthew Brennan Jones",
    author_email = "matthew.brennan.jones@gmail.com",
    description = "Get CPU info with pure Python 2 & 3",
    long_description=readme_content,
    license = "MIT",
    url = "https://github.com/workhorsy/py-cpuinfo",
    packages=['cpuinfo'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ],
)


