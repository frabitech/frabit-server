# (c) 2020 frabit-server Project maintained and limited by FrabiTech < blylei.info@gmail.com >
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# This file is part of frabit-server
#
"""Backup and Recovery Manager for MySQL

Frabit (Fly rabbit) is an open-source administration tool for disaster recovery of MySQL servers written in Python.
It allows your organisation to perform remote backups of multiple servers in business critical environments to reduce
risk and help our DBAs during the recovery phase.
"""

import sys

from setuptools import find_packages, setup

if sys.version_info < (3, 6):
    raise SystemExit('ERROR: Frabit needs at least python 3.6 to work')

# Depend on pytest_runner only when the tests are actually invoked
needs_pytest = set(['pytest', 'test']).intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []

setup_requires = pytest_runner

install_requires = [
    'mysql-connector-python >= 8.0.22',
    'argh >= 0.21.2',
    'python-dateutil',
]

if sys.version_info < (2, 7):
    install_requires += [
        'argparse',
    ]
    # If we are going to execute tests, we need to enforce wheel
    # version before installing mock, or it will fail
    if needs_pytest:
        setup_requires += [
            'wheel<0.30.0',  # wheel has dropped 2.6 support in 0.30.0
        ]

frabit = {}
with open('frabitd/version.py', 'r') as version:
    exec(version.read(), frabit)

setup(
    name='frabit-server',
    version=frabit['__version__'],
    author='FrabiTech Limited',
    author_email='blylei.info@gmail.com',
    url='https://github.com/frabitech/frabit-server',
    packages=find_packages(exclude=["tests"]),
    entry_points={
        'console_scripts': [
            'frabitd=frabit.cli:main',
        ],
    },
    license='GPL-3.0',
    description=__doc__.split("\n")[0],
    long_description="\n".join(__doc__.split("\n")[2:]),
    install_requires=install_requires,
    extras_require={
        'completion': ['argcomplete'],
    },
    platforms=['Linux'],
    classifiers=[
        'Environment :: Console',
        'Development Status :: 4 - Beta',
        'Topic :: System :: Archiving :: Backup',
        'Topic :: Database',
        'Topic :: System :: Recovery Tools',
        'License :: OSI Approved :: GNU General Public License v3 or later '
        '(GPLv3+)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: POSIX :: Linux'
    ],
    setup_requires=setup_requires,
    tests_require=[
        'mock',
        'pytest-timeout',
        'pytest',
    ],
)
