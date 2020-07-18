from pwn import *
from math import gcd

r = remote('ctf-chall-dev.csivit.com', 30827)

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

for i in range(10):
    inp=r.recv(100).decode()

    print(inp)

    if 'csictf' in inp or 'Nahh' in inp:
        break
    else:
        try:
            a, b = list(map(int, inp.split(" ")))

            print(a, b)
            x=fact(gcd(a,b)+3)
            print("a = {}, b = {}, x = {}".format(a, b, x))
            r.sendline(str(x))
        except ValueError:
            pass
