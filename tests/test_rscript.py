# -*- coding: utf-8 -*-
import os
import pytest
import time

from pyRscript import pyRscript
from collections import namedtuple


@pytest.fixture
def rscript():
    RPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'R')
    CMD = '-d,SN1234,-t,2017-07-13 00:00:00'
    r = pyRscript.Rscript(path=RPATH, file='test.R', cmd=CMD)
    return r


def test_repr(rscript):
    RPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'R')
    CMD = '-d,SN1234,-t,2017-07-13 00:00:00'
    assert str(rscript) == '<Parameter test.R {} {}>'.format(RPATH, CMD.split(','))


def test_script(rscript):
    ret = rscript.execute()
    assert str(type(ret)) == "<class 'pyRscript.pyRscript.ParsedCompletedCommand'>"
    assert ret.returncode == 0


def test_decode_cmd_out(rscript):
    ParsedCompletedCommand = namedtuple(
        'ParsedCompletedCommand',
        ['returncode', 'args', 'stdout', 'stderr']
    )
    c = ParsedCompletedCommand(
            args=['Rscript', 'test.R', '-d', 'SN1234', '-t', '2017-07-13 00:00:00'], 
            returncode=0, 
            stdout=b'test',
            stderr=b'test'
        )
    assert repr(rscript.decode_cmd_out(c)) == "ParsedCompletedCommand(returncode=0, args=['Rscript', 'test.R', '-d', 'SN1234', '-t', '2017-07-13 00:00:00'], stdout='test', stderr='test')"