# -*- coding: utf-8 -*-
"""
    pyRscript
    ~~~~

    It's a easy tool to use subprocess call Rscript and execute R program and return returncode, stdout, stderr. 

    :copyright: (c) 2017 by chairco <chairco@gmail.com>.
    :license: BSD.
"""

import uuid

from pip.req import parse_requirements  
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

import pyRscript


def requirements(path):  
    return [str(r.req) for r in parse_requirements(path, session=uuid.uuid1())]


class Tox(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['-v', '-epy']
        self.test_suite = True

    def run_tests(self):
        import tox
        tox.cmdline(self.test_args)


setup(  
    name='pyRscript',
    version=pyRscript.__version__,
    author=pyRscript.__author__,
    author_email=pyRscript.__email__,
    url='https://github.com/chairco/pyRscript',
    description='easy tool to use subprocess call Rscript and execute R program.',
    long_description=__doc__,
    packages=find_packages(),
    install_requires=requirements('requirements.txt'),
    tests_require=['tox'],
    cmdclass={'test': Tox},
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Documentation',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)