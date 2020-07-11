
# Escape Plan

Authors: [alias-rahil](https://github.com/alias-rahil)

## Description

Another pyjail challenge with a little twist at the end to find the flag.

# Requirements

- Python
- Docker

## Sources

- None

```
I found a script that solves ciphers, they say it's pretty secure!
```

# Exploit

It is a python file running on a netcat listener which can encode/decode crypto ciphers. The user can notice that it can not only call the cipher functions mentioned in the examples but can also run all the python built-in functions. He will then use `__import__('os').system('sh')` to spawn a shell. After finding the repository link from `.git/config`, he should be able to find the flag by checking the older commits. The flag is in a `.env` file, which was deleted in the later conmits.
 
The Flag is:
```
csictf{2077m4y32_h45_35c4p3d}
```
