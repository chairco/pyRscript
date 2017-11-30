# pyRscript

It's a easy tool to use subprocess call Rscript and execute R program and return returncode, stdout, stderr.

Sample Usage:
```
>> r = Rscript(file='test.R', cmd='-t,tlcd0501,-s,2017-07-13 00:00:00,-e,2017-07-14 00:00:00', folder='R')
>> print(r)
>> <RETURN: ParsedCompletedCommand(returncode=0, args=['Rscript', ...
>> r = Rscript(file='test.R')
>> print(r)
>> <ParsedCompletedCommand(returncode=1, args=['Rscript', ...
```

## Install


## Test


## Lincese

