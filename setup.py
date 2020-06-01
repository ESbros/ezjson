import codecs
import os
from setuptools import find_packages, setup

PACKAGE_NAME = "ezjson"
VERSION = "0.1.0"
AUTHOR = "Erik Solis"
AUTHOR_EMAIL = "edsg77@gmail.com"
DESCRIPTION = "EZ-JSON is a domain-specific language to create JSON files in an easier way"
KEYWORDS = "textX DSL python domain specific languages JSON files generation"
LICENSE = "MIT"
URL = "https://github.com/ESbros/ezjson.git"
setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    url=URL,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    keywords=KEYWORDS,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True,
    package_data={"": ["*.tx"]},
    install_requires=["textx_ls_core"],
    entry_points={"textx_languages": ["ezjson = tx_ezjson:ezjson"]},
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
    ],
)
