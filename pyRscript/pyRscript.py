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
    >> RPATH = '/home/pyRscript' # also ex: os.path.join(os.path.dirname(os.path.abspath('test.R')), 'R')
    >> cmd = '-d,SN1234,-t,2017-07-13 00:00:00'
    >> r = pyRscript.Rscript(path=RPATH, file='test.R', cmd=cmd)
    >> print(r)
    >> <Parameter test.R /home/pyRscript ['-d', 'SN1234', '-t', '2017-07-13 00:00:00']>
    >> ret = r.execute()
    >> print(ret)
    >> ParsedCompletedCommand(returncode=0, args=['Rscript', 'test.R', '-d', 'SN1234', '-t', '2017-07-13 00:00:00'], stdout='2017-12-03 11:35:38 INFO::Execute R\n2017-12-03 11:35:39 INFO::id: SN1234, time: 2017-07-13 00:00:00', stderr='Loading required package: methods')
    >> print(ret.returncode)
    >> 0
    >> print(ret.stdout)
    >> '2017-12-03 11:37:59 INFO::Execute R\n2017-12-03 11:37:59 INFO::id: SN1234, time: 2017-07-13 00:00:00'
    >> print(ret.stderr)
    >> 'Loading required package: methods'
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


