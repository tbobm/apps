"""Packaging file for webserver."""
from setuptools import find_packages
from distutils.core import setup


__version__ = "0.0.0"

setup(
    name="base-webserver",
    packages=["webserver"],
    # NOTE: could be dynamically generated using requirements.txt
    install_requires=['Flask'],
    version=__version__,
    author="Theo 'Bob' Massard",
    author_email="tbobm@protonmail.com",
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    entry_points={
        "console_scripts": [
            "webserver-run-cli=webserver.app:main",
        ],
    },
)
