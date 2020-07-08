# Challenge Name

Author: [pragati1610](https://github.com/pragati1610)

## Description

This is a crypto challenge using serpent cipher

## Requirements

- Docker: [Dockerfile](./Dockerfile)

## Sources

- [sample.py](./sample.py)
- [sample.txt](./sample.txt)

```
I am stuck on the CBC's base for 3 months now. I somehow got my hands on this pair of transmitter and receiver. I sent out some signals to my home base and in a few minutes i received an encrpted message. Coud you help me decrypt it please?

the message :

qncZjO3+gURGQ8uz1rKtJ0DLmVRYatHd0+bN6S5If/S8sb18ZER+QYAbn8MfLmr0yhEuA7o1YNB5oN5uBMHI2w==

Hint 1: Which language is the challenge's name in?? - Points 100
```

## Exploit

Decrypt the message using serpent - the algo used to encrypt the message.
You will require the key which is the language the challenge name is in i.e. russian

The flag is:
csictf{l34v3_th3_b4s3_4t_f0ur_4nd_3_qu4rt3rs}
```
