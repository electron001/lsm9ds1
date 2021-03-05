import os
from setuptools import setup, find_packages

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except:
    long_description = ''

classifiers = ['Development Status :: 4 - Beta',
               'Operating System :: POSIX :: Linux',
               'License :: OSI Approved :: Apache Software License',
               'Intended Audience :: Developers',
               'Programming Language :: Python :: 3.8',
               'Topic :: Software Development',
               'Topic :: System :: Hardware']

setup(
    name         = 'lsm9ds1_python',
    version      = '1.0.1',
    author       = 'Maciej Biskup',
    author_email = 'mbiskup123@gmail.com',
    description  = "Library for lsm9ds1",
    long_description=long_description,
    #url          = 'https://github.com/FaBoPlatform/FaBo9AXIS-MPU9250-Python/',
    license      = 'GNU General Public License v3.0',
    classifiers  = classifiers,
    packages     = find_packages()
)
