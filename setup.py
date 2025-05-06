"""Setup script for the demo package."""

from setuptools import setup, find_packages

setup(
    name="demo",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Flask",
    ],
    entry_points={
        "console_scripts": [
            "demo=demo.cli:main",
        ],
    },
)