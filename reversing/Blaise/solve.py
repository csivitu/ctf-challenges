from pwn import *

r = remote('localhost', 3000)
n = int(r.recv(100).decode())

def nCr(n, r):
    return str(int(fact(n) / (fact(r) * fact(n - r))))
  
def fact(n): 
    res = 1
    for i in range(2, n+1): 
        res = res * i     
    return res 

for i in range(n+1):
    print(nCr(n,i))
    r.sendline(nCr(n,i))

print(r.recv().decode())
