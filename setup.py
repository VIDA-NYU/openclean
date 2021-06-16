# This file is part of the Data Cleaning Library (openclean).
#
# Copyright (C) 2018-2021 New York University.
#
# openclean is released under the Revised BSD License. See file LICENSE for
# full license details.

"""Required packages for install, test, docs, and tests."""

from setuptools import setup, find_packages


install_requires = [
    'openclean-core==0.4.1'
]

docker_requires = ['docker']

geo_requires = ['openclean-geo==0.1.0']
metanome_requires = ['openclean-metanome==0.2.0']
notebook_requires = ['openclean-notebook==0.1.5']
pattern_requires = ['openclean-pattern==0.0.1']
openclean_extension = geo_requires + metanome_requires + notebook_requires + pattern_requires

extras_require = {
    'demo': openclean_extension + ['jupyter', 'humanfriendly', 'ethiopian_date', 'seaborn'],
    'docker': docker_requires,
    'jupyter': ['jupyter'],
    'geo': geo_requires,
    'metanome': metanome_requires,
    'notebook': notebook_requires,
    'pattern': pattern_requires,
    'full': docker_requires + openclean_extension
}


# Get long project description text from the README.rst file
with open('README.rst', 'rt') as f:
    readme = f.read()


setup(
    name='openclean',
    version='0.2.0',
    description='Library for data cleaning and data profiling',
    long_description=readme,
    long_description_content_type='text/x-rst',
    keywords='data cleaning, data profiling',
    url='https://github.com/VIDA-NYU/openclean',
    author='New York University',
    author_email='heiko.muller@gmail.com',
    license='New BSD',
    license_file='LICENSE',
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    extras_require=extras_require,
    install_requires=install_requires,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python'
    ]
)
