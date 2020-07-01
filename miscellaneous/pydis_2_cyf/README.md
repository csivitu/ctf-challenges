
# Some name

Authors: [Atharva](https://github.com/Atharva-Gundawar)

Disassemble Python byte code and reverse the obtained python code.

# Requirements

- Python 3
- Basic Knowledge of Python Byte Code


Files: py_dis1, encodedflag.txt
```

# Exploitation

The code you see in [`py_dis`]('./py_dis) is essentially python bytecode. The target in this challenge is to reverse this program and pass the string in [`snake.txt`](./py_dis) as input, so that we get the flag.

```
## Sources

- [py_dis](./py_dis)
- [encodedflag.txt](./encodedflag.txt)

## Challenge description to go up on the website.

Hint 1: python disassembly is easy  - Points 100
Hint 2: pip install Assembly - Points 200/300

## Exploit

<!-- Much more detailed description than the following. -->
Reverse `py_dis` to decrypt the flag in `encodedflag.txt` .
The `py_dis`  File will be the reversed version of 2 layers of Substituion Ciphers:

 - Substitution acording to occurance : For any given char if n is the number of times it occurs then it would be replacd by chr(x+n) where x is the ascii value of the char
 
 - Some other popular and known ciphers 

 
## The Flag:
csictf{T#a+_wA5_a_g0oD_0n3_YaY}
Feel free to change this XD
