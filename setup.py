# setup.py
from setuptools import setup, find_packages

setup(
    name='lego_analyzer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'matplotlib'
    ],
    entry_points={
        'console_scripts': [
            'lego_cli=lego_cli.main:main'
        ]
    }
)
