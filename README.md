# pyRscript

It's a easy tool to use subprocess call Rscript and execute R program and return returncode, stdout, stderr.

Sample Usage:
```
>> import os
>> from pyRscript import pyRscript
>> RPATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'R')
>> r = pyRscript.Rscript(path=RPATH, file='test.R', cmd='-t,tlcd0501,-s,2017-07-13 00:00:00,-e,2017-07-14 00:00:00')
>> print(r)
>> <ParsedCompletedCommand(returncode=1, args=['Rscript', ...
```

## Install


## Test


## Lincese

