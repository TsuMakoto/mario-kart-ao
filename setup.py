# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='mario_kart_ai',
    version='0.1.0',
    description='Mario Kart AI',
    long_description=readme,
    author='TsuMakoto',
    url='https://github.com/TsuMakoto/mario-kart-ai',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

