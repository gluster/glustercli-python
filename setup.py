import os
import re
from setuptools import setup

VERSION = "0.8.0"


setup(
    name='glustercli',
    version=VERSION,
    description='Python bindings for GlusterFS CLI and Metrics collection',
    license='GPLv2 or LGPLv3+',
    author='Aravinda Vishwanathapura',
    author_email='aravinda@kadalu.io',
    url='https://github.com/gluster/glustercli-python',
    packages=["glustercli", "glustercli.cli", "glustercli.metrics"],
    install_requires=["paramiko"],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',  # noqa
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: System :: Filesystems',
    ],
)
