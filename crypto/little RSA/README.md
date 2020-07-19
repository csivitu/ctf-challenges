# little RSA

Author: [pragati1610](https://github.com/pragati1610)

## Description

Wiener's attack is a modified version of RSA with the value of private key exponent is comparatively small to the value of N(the product of primes).
This challenge is a simple Wiener's attack challenge which has given the values of n and e and the encrypted message, which then has to be decrypted by the private key exponent d and that can be found out by n and e using Wiener's approximation.

## Requirements

- Docker: [Dockerfile](./Dockerfile)

## Sources

- [flag.zip](./flag.zip)
- [a.txt](./a.txt)

```
The flag.zip contains the flag I am looking for but it is password protected. The password is the encrypted message which has to be correctly decrypted so I can use it to open the zip file. I tried using RSA but the zip doesn't open by it. Can you help me get the flag please? 

Hint 1: Try applying Wiener's attack approximations. - Points 100
```

## Exploit
```
. a.txt contains 3 numbers namely :

the message c = 32949
n = 64741
public encryption key e = 42667

. Wieners approximation gives :

phi(n) ~(approximately equal to) n -----(1)
and from 
    ed = k.phi(n)+1
    i.e. e/phi(n) = k/d + 1/(d.phi(n))
compared to the other terms 1/(d.phi(n)) is negligible and from (1)
we get:
    e/n ~(approximately equal to) k/d

. We need to find an approximation to 
e/n = 42667/64741 so that we can find k/d but we have some conditions : 
1. if ed = k.phi(n)+1 then phi(n) is even and d has to be odd
2. phi(n)=(ed-1)/k has to be a whole number because phi(n) is essentially the product of 2 whole numbers (p-1) and (q-1)

. Using continued fractions (Applying Euclidian Algorithm):

42667/64741 = 0 ; rem = 42667
=> k/d ~ 0/1 
but k=0 and d=1 can not work for decryption so we go to the next convergent

64741/42667 = 1 ; rem = 22074
=> k/d ~ 1/1
but k=1 and d=1 can again not work for decryption so we go to the next convergent

42667/22704 = 1 ; rem = 20593
=> k/d ~ 1/2
but k=1 and d=2 can again not work because d is even and the conditions mentioned d to be odd.

22074/20593 = 1 ; rem = 1481
=> k/d ~ 2/3
k=2 and d=3 ----d is odd (passes one condition)
phi(n) = (ed-1)/k = 64000 ----which is a whole number(passes second condition)

Using this d we can decrypt the message :
c=32949
so using any online RSA calculator we can find m = 18429

. Use this password to open the zip file and subsequently find the flag in flag.txt in the unzipped file.
```

<br />

The flag is:
csictf{gr34t_m1nds_th1nk_4l1ke}