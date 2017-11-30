# pyRscript

It's a easy tool to use subprocess call Rscript and execute R program and return returncode, stdout, stderr.

Sample Usage:
```
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
```


## Install

```
$ git clone https://github.com/chairco/pyRscript
$ cd pyRscript
$ pyton setup.py install
```


## Test

```
python -m pytest
```


## Lincese

MIT LICENSE

