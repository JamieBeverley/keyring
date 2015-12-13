#!/usr/bin/env python
# Generated by jaraco.develop 2.27.1
# https://pypi.python.org/pypi/jaraco.develop

import io
import sys

import setuptools

with io.open('README.rst', encoding='utf-8') as readme:
    long_description = readme.read()

needs_pytest = {'pytest', 'test'}.intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []
needs_sphinx = {'release', 'build_sphinx', 'upload_docs'}.intersection(sys.argv)
sphinx = ['sphinx'] if needs_sphinx else []
needs_wheel = {'release', 'bdist_wheel'}.intersection(sys.argv)
wheel = ['wheel'] if needs_wheel else []

test_requirements = [
    'pytest>=2.8',
    'gdata',
    'python-keyczar',
    'fs>=0.5',
    'mock',
    'pycrypto',
]
"dependencies for running tests"

if sys.version_info < (2, 7) or (
        sys.version_info >= (3, 0) and sys.version_info < (3, 1)):
    # Require unittest2 for Python which doesn't contain the new unittest
    # module (appears in Python 2.7 and Python 3.1)
    test_requirements.append('unittest2')

if sys.version_info >= (3, 0):
    # gdata doesn't currently install on Python 3. Omit it also.
    # http://code.google.com/p/gdata-python-client/issues/detail?id=229
    test_requirements.remove('gdata')

    # keyczar doesn't currently install on Python 3. Omit it also.
    # http://code.google.com/p/keyczar/issues/detail?id=125
    test_requirements.remove('python-keyczar')

setup_params = dict(
    name='keyring',
    use_scm_version=True,
    author="Kang Zhang",
    author_email="jobo.zh@gmail.com",
    maintainer='Jason R. Coombs',
    maintainer_email='jaraco@jaraco.com',
    description="Store and access your passwords safely.",
    long_description=long_description,
    url="https://github.com/jaraco/keyring",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
    ],
    extras_require={
        'test': test_requirements,
    },
    setup_requires=[
        'setuptools_scm>=1.9',
    ] + pytest_runner + sphinx + wheel,
    tests_require=[
    ] + test_requirements,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Python Software Foundation License",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
    ],
    entry_points={
        'console_scripts': [
            'keyring=keyring.cli:main',
        ],
    },
    keywords="keyring Keychain GnomeKeyring Kwallet password storage",
)
if __name__ == '__main__':
    setuptools.setup(**setup_params)
