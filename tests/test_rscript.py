# -*- coding: utf-8 -*-
import os
import pytest

from pyRscript import pyRscript

@pytest.fixture
def rscript():
    RPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'R')
    CMD = '-t,tlcd0501,-s,2017-07-13 00:00:00,-e,2017-07-14 00:00:00'
    r = pyRscript.Rscript(path=RPATH, file='test.R', cmd=CMD)
    return r


def test_repr(rscript):
    RPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'R')
    CMD = '-t,tlcd0501,-s,2017-07-13 00:00:00,-e,2017-07-14 00:00:00'
    assert str(rscript) == '<Parameter test.R {} {}>'.format(RPATH, CMD.split(','))


def test_script(rscript):
    ret = rscript.execute()
    assert str(type(ret)) == "<class 'pyRscript.pyRscript.ParsedCompletedCommand'>"
    assert ret.returncode == 0