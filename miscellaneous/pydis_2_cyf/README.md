# PYDIS_2_CTF

Authors: [21StWarlock#1598](21StWarlock#1598)

Disassemble Python byte code and reverse the obtained python code.

# Requirements

- Python 3
- Basic Knowledge of Python Byte Code

Files: dis_code, encodedflag.txt
```
# Exploitation

The code you see in [C1cipher](./C1cipher) and [C2cipher](./C2cipher) is essentially python bytecode. The target in this challenge is to reverse this programs and pass the string in [`encodedflag.txt`](./py_dis) as input, so that we get the flag.

```
## Sources

- [C1cipher](./C1cipher)
- [C2cipher](./C2cipher)
- [encodedflag.txt](./encodedflag.txt)


```
Assemble and reverse 2 ciphers to get the flag
Hint 1: python disassembly is easy  - Points 100
Hint 2: pip install Assembly - Points 200
```

## Exploit

There are two ciphers in [C1cipher](./C1cipher) and [C2cipher](./C2cipher) and you have two convery both the ciphers into python code the solution is in [Solution](https://github.com/csivitu/ctf-challenges/tree/master/miscellaneous/PYDIS_2_CTF/solution.txt)

 The flag is:
```
csictf{T#a+_wA5_g0oD_d155aSe^^bLy}
```