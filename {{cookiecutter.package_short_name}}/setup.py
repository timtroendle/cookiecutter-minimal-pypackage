#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(
    name='{{ cookiecutter.package_short_name }}',
    version='{{ cookiecutter.version }}',
    description='{{ cookiecutter.short_description }}',
    maintainer='{{ cookiecutter.author }}',
    maintainer_email='{{ cookiecutter.email }}',
    url='https://www.github.com/{{ cookiecutter.github_name }}/{{ cookiecutter.package_short_name }}',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=[],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering'
    ]
)
