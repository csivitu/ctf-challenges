# Quick Math
Author: [ashikka](https://github.com/ashikka)

## Description

Hastad's attack and the Chinese Remainder Theorem.

## Requirements 

- RSA
- Chinese Remainder Theorem

## Sources

```
Ben has encrypted a message with the same value of 'e' for 3 public moduli -
n1 = 86812553978993
n2 = 81744303091421 
n3 = 83695120256591 
and got the cipher texts - 
c1 = 8875674977048
c2 = 70744354709710
c3 = 29146719498409.
Find the original message. (Wrap it with csictf{})
```


## Exploit

In this challenge, on seeing the values: n, c, e, we can guess that it involves RSA encryption. We have to use The Chinese Remainder Theorem to find out the `p^e`, which is the original message raised to the power of a prime number `e` (in this case, 3). 

```
p^e = 8875674977048 (mod 86812553978993)
p^e = 70744354709710 (mod 81744303091421)
p^e = 29146719498409 (mod 83695120256591)
```

You can use [dcode.fr](https://www.dcode.fr/chinese-remainder) to find the value of `p^e`. Now, we compute it's cube root to get a 12 digit string. This string has been encoded to hex, on decoding we get.

```python
>>> bytes.fromhex('683435743464')
b'h45t4d'
```

The flag is:

```
csictf{h45t4d}
```
