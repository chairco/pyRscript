[![Documentation Status](https://readthedocs.org/projects/pyrscript/badge/?version=latest)](http://pyrscript.readthedocs.io/en/latest/?badge=latest)

# pyRscript

It's a easy tool to use subprocess call `Rscript` and execute R program then get the return's information: `returncode`, `stdout`, `stderr`.

Be careful of this is running R on your device machine not vritual machine, be sure the R enivronmet is good on your computer.


Parameter:
+ path: the target R's absolute path.
+ file: R program.
+ cmd: Not necessary but if need parameter use str and split with comma(`,`).


Sample Usage:
```
>> import os
>> from pyRscript import pyRscript
>> RPATH = '/home/pyRscript'
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
```


## Install

```
$ pip install pyRscript
```


## Test

```
python -m pytest
```


## Lincese

MIT LICENSE

