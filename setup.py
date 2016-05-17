# -*- coding: utf-8 -*-

from setuptools import setup


__version__ = '0.1.0'

setup(
    name='Sig',
    version=__version__,
    author='Sérgio Rafael Siqueira',
    author_email='sergio@inbep.com.br',
    tests_require=[
        'Jinja2>=2.8',
        'Logbook>=0.12.5',
        'nose>=1.3.7'
    ]
)
