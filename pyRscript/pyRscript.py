# -*- coding:utf-8 -*-
import subprocess as sp
import os
import time

from contextlib import contextmanager
from collections import OrderedDict, namedtuple


ParsedCompletedCommand = namedtuple(
    'ParsedCompletedCommand',
    ['returncode', 'args', 'stdout', 'stderr']
)


class Rscript:
    """
    Using subprocess to call Rscript execute R program
    :type file: str, target R file
    :type cmd: str, parameter of target R file 
    :type folder: str, default '', only support the sub folder 

    example:
    >> import os
    >> from pyRscript import pyRscript
    >> RPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'R')
    >> cmd = '-t,tlcd0501,-s,2017-07-13 00:00:00,-e,2017-07-14 00:00:00'
    >> r = pyRscript.Rscript(path=RPATH, file='test.R', cmd=cmd)
    >> print(r)
    >> <Parameter test.R /Users/chairco/OneDrive/SourceCode/python/pyRscript/pyRscript/R ['-t', 'tlcd0501', '-s', '2017-07-13 00:00:00', '-e', '2017-07-14 00:00:00']>
    >> ret = r.execute()
    >> print(ret)
    >> ParsedCompletedCommand(returncode=0, args=['Rscript', 'test.R', '-t', 'tlcd0501', '-s', '2017-07-13 00:00:00', '-e', '2017-07-14 00:00:00'], stdout='2017-11-30 22:45:15 INFO::execute ROT...\n2017-11-30 22:45:15 INFO::tid: tlcd0501, st: 2017-07-13 00:00:00, et: 2017-07-14 00:00:00', stderr='Loading required package: methods')
    >> print(ret.returncode)
    >> 0
    >> print(ret.stdout)
    >> '2017-11-30 22:45:15 INFO::execute ROT...\n2017-11-30 22:45:15 INFO::tid: tlcd0501, st: 2017-07-13 00:00:00, et: 2017-07-14 00:00:00'
    >> print(ret.stderr)
    >> 'Loading required package: methods') <class '__main__.ParsedCompletedCommand'
    """

    def __init__(self, path, file, cmd=None):
        super(Rscript, self).__init__()
        self.file = file
        self.path = path
        if cmd is None:
            self.cmd = []
        else:
            self.cmd = cmd.split(',')

    @contextmanager
    def cd(self, newdir):
        """
        go to the path
        """
        prevdir = os.getcwd()
        os.chdir(newdir)
        try:
            yield
        finally:
            os.chdir(prevdir)

    def decode_cmd_out(self, completed_cmd):
        """
        return a standard message
        """
        try:
            stdout = completed_cmd.stdout.encode('utf-8').decode()
        except AttributeError:
            stdout = str(bytes(completed_cmd.stdout), 'big5').strip()
        try:
            stderr = completed_cmd.stderr.encode('utf-8').decode()
        except AttributeError:
            stderr = str(bytes(completed_cmd.stderr), 'big5').strip()
        return ParsedCompletedCommand(
            completed_cmd.returncode,
            completed_cmd.args,
            stdout,
            stderr
        )

    def run_command_under_r_root(self, cmd, catched=True):
        """
        subprocess run on here
        """
        RPATH = self.path
        with self.cd(newdir=RPATH):
            if catched:
                process = sp.run(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
            else:
                process = sp.run(cmd)
            return process

    def execute(self):
        """
        Execute R script
        """
        rprocess = OrderedDict()
        commands = OrderedDict([
            (self.file, ['Rscript', self.file] + self.cmd),
        ])
        for cmd_name, cmd in commands.items():
            rprocess[cmd_name] = self.run_command_under_r_root(cmd)
        
        return self.decode_cmd_out(completed_cmd=rprocess[self.file])

    def __repr__(self):
        fmt = f'<Parameter {self.file} {self.path} {self.cmd}>'
        return fmt


