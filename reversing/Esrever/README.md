# Esrever

Author: [roerohan](https://github.com/roerohan)

## Description

This is a reversing challenge.

## Requirements

- Python

## Sources

- [esrever.py](./esrever.py)
- [esrever.txt](./esrever.txt)

```
I encrypted my flag so that nobody can see it, but now I realize I don't know how to decrypt it. Can you help me?
```

## Exploit

This challenge seems to have a lot of random numbers, but the encryption is entirely predictable. The solution script is specified in [solve.py](./solve.py).

```bash
$ python solve.py | grep csictf
csictfaesreverisjustreverseinreverserightc
```

You can now just guess that `{` became `a` and `}` became `c` due to `enc1()`, since it shifts every character in the range of `'a'` to `'z'`.

The flag is:

```
csictf{esreverisjustreverseinreverseright}
```