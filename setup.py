#
# @filename    : setup.py
# @description : The traditional setup.py script for
#                Installation from pip or easy_install

from codecs import open
from setuptools import setup

with open("README.md", "r") as file:
    long_description = file.read()

setup(
    name='crypton',
    version='1.0.0',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/OverwatchHeir/CryptOn.git',
    download_url='https://github.com/OverwatchHeir/CryptOn/archive/master.zip',
    author='OverwatchHeir',
    author_email='softw.dev@protonmail.com',
    license="GNU",
    install_requires=[
        'termcolor',
        'cryptography',
        'pycrypto',
        'validate_email',
        'py3dns',
        'requests'
    ],
    packages=['crypton'],
    include_package_data=True,
    data_files=['crypton/wordlist.txt'],
    classifiers=[
        'Topic :: Utilities',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7'
    ],
    entry_points={
        'console_scripts': ['crypton = crypton.crypton:main']
    }

)
