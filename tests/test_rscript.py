# -*- coding: utf-8 -*-
import os
import pytest

from pyRscript import pyRscript


def test_script():
    RPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'R')
    r = pyRscript.Rscript(path=RPATH, file='test.R', cmd='-t,tlcd0501,-s,2017-07-13 00:00:00,-e,2017-07-14 00:00:00')
    assert str(type(r)) == "<class 'pyRscript.pyRscript.Rscript'>"  