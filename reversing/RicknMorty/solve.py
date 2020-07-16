from pwn import *

r = remote('localhost', 3000)


def fact(n):
    if n==1:
        return n
    else:
        return n * fact(n-1)

def hcf(a,b):
    hcf = 0
    for i in range(1,max(a,b)): 
        if( a%i == 0 and  b%i == 0 ):
            hcf = i
    return hcf


for i in range(500):
    inp=r.recv(100).decode()

    if 'fun()' in inp:
        print(inp)
    
    elif 'csictf' in inp:
        print(inp)
        break

    else:
        a, b = list(map(int, inp.split(" ")))

        print(a, b)
        x=fact(hcf(a,b)+3)
        print("a = {}, b = {}, x = {}".format(a, b, x))
        r.sendline(str(x))
