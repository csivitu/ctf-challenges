# Login Error

Author: [harsoh](https://github.com/harsoh)

## Description

Challenge based on AES-CBC bit flipping attack.

## Requirements

- Docker: [Dockerfile](./Dockerfile)

## Sources

- [ques.py](./ques.py)
- [sol.py](./sol.py)

```
We forgot our credentials, help us to get the flag.

```

## Exploit

The server is running a python script. The program tells that it uses AES and it is a very classic problem of changing the encryption so that some specific changes happen after decryption which can be done by bit flipping attack. The username is given to be similar to c?i and password to c?f, it is trivial that they are csi and ctf respectively. The changes need to happen in 2 encryptions, both at the 6th indices, like in any bit flipping attack we xor the current plaintext value at 6th index('?') and the wanted plaintext value at 6th index('s' and 't') and then xor the resultant value with 6th index of previous block.
<br /> 

The flag is:

```
csictf{Sh4u!d_hav3_n0t_u5ed_CBC}
```
