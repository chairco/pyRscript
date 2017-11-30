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
    >> r = Rscript(file='test.R', cmd='-t,tlcd0501,-s,2017-07-13 00:00:00,-e,2017-07-14 00:00:00', folder='R')
    >> print(r)
    >> <RETURN: ParsedCompletedCommand(returncode=0, args=['Rscript', ...
    >> r = Rscript(file='test.R')
    >> print(r)
    >> <ParsedCompletedCommand(returncode=1, args=['Rscript', ...
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
        subprocess
        """
        RPATH = self.path
        with self.cd(newdir=RPATH):
            if catched:
                process = sp.run(cmd, stdout=sp.PIPE, stderr=sp.PIPE)
            else:
                process = sp.run(cmd)
            return process

    @property
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
        return rprocess

    def __repr__(self):
        ret = self.execute
        message = self.decode_cmd_out(completed_cmd=ret[self.file])
        fmt = f'<{message}>'
        return fmt

if __name__ == '__main__':
    RPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'R')
    r = Rscript(path=RPATH, file='test.R', cmd='-t,tlcd0501,-s,2017-07-13 00:00:00,-e,2017-07-14 00:00:00')
    print(r)