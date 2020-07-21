# Challenge Name

Author: [Pragati](https://github.com/pragati1610)

## Description

You have been given the byte code of a python code with the encrypted flag. Find the python code, reverse it and use it to decrypt the encrypted flag.

## Requirements

- None

## Sources

- [bytecode.txt](./bytecode.txt)
- [flag.txt](./flag.txt)

```
I need to decrypt the flag, but the code to encrypt it is in byte code. Will you help me reverse it and decrypt the flag? 

```

## Exploit

The long way:

Using any online compiler that shows the byte code for a python program understand how loops like for work, how does assignment operation, addition, multiplication etc work.

Then try writing the encrypt function. [revQ.py](./revQ.py)

Decryption function is almost the same except you will have to divide by 3 this time

Use decryption function to decrypt the flag

The short way:

Once you find that the by dividing(integer division) each letter in the encrypted flag by 3 and subsequently finding the characters corresponding to the ascii values of each letter, which can be rearranged intuitively to get the flag.

<br />

The flag is:
csictf{t4th_w4s_qu1ck!}
