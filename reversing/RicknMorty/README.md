# RickNMorty

Author: [Atharva-Gundawar](https://github.com/Atharva-Gundawar/)

## Description

This is a reversing challenge, can be solved using any decompiler / dissasembler.

## Requirements

- Docker: [Dockerfile](./Dockerfile)
- ghidra

## Sources

- [RickNMorty](./bin/RickNMorty)

```
Rick has been captured by the council of ricks and in this dimmention morty has to save him, the chamber holding rick needs a key . Can you help him find the key ? 
```

## Exploit

Open `ghidra` and analyze the binary. You can see the following main function:

```

undefined8 main(void)

{
  int iVar1;
  time_t tVar2;
  ulong uVar3;
  long lVar4;
  int local_4c;
  time_t local_48;
  time_t local_40;
  time_t local_38;
  uint local_30;
  uint local_2c;
  char *local_28;
  int local_20;
  int local_1c;
  
  setbuf(stdout,(char *)0x0);
  setbuf(stdin,(char *)0x0);
  setbuf(stderr,(char *)0x0);
  tVar2 = time(&local_38);
  srand((uint)tVar2);
  time(&local_40);
  local_1c = 1;
  local_20 = 0;
  while( true ) {
    iVar1 = rand();
    if (iVar1 % 400 + 100 <= local_20) break;
    iVar1 = rand();
    local_2c = iVar1 % 10 + 6;
    iVar1 = rand();
    local_30 = iVar1 % 10 + 6;
    printf("%d %d",(ulong)local_2c,(ulong)local_30);
    __isoc99_scanf();
    uVar3 = function1(local_2c,local_30);
    lVar4 = function2((int)uVar3 + 3);
    if ((long)local_4c != lVar4) {
      local_1c = 0;
    }
    local_20 = local_20 + 1;
  }
  time(&local_48);
  local_28 = (char *)(double)(local_48 - local_40);
  printf(local_28,"fun() took %f seconds to execute \n");
  if ((local_1c == 1) && ((double)local_28 <= 5.00000000)) {
    system("cat flag.txt");
  }
  return 0;
}


```

So at first look we can see that there is a time limit of 5 sec for the program to run , and that two random numbers `local_2c` and `local_30` are ouptupted which are in turn processed by the following functions and if the value of the number returned is what the user inputs for all casses then the the flag is outputed :
<br />

The first function is called function 1 and it consits of : 

```

ulong function1(uint param_1,uint param_2)

{
  uint local_10;
  uint local_c;
  
  local_c = 0;
  local_10 = 1;
  while ((local_10 <= param_1 || (local_10 <= param_2))) {
    if ((param_1 % local_10 == 0) && (param_2 % local_10 == 0)) {
      local_c = local_10;
    }
    local_10 = local_10 + 1;
  }
  return (ulong)local_c;
}

```
You can see that this code starts a loop from 0 to the min of the 2 variables passed to it, then it finds the largest nuber which divides both of them .
In short this is an HCF function
<br />

The second function is called function 2 and it consits of : 

```

long function2(uint param_1)

{
  long lVar1;
  
  if (param_1 == 0) {
    lVar1 = 1;
  }
  else {
    lVar1 = function2(param_1 - 1);
    lVar1 = lVar1 * (ulong)param_1;
  }
  return lVar1;
}

```
You can see that these lines of code is a code for a factorial function

<br />

In essence, the program initially displays 2 random number `a` and `b`, between 10 and 16, and then expects the values of the factorial of its HCF random number of times between 100 and 500. If all these match in a given time limmit of 5 seconds , it prints the flag. We can write a [python script](./solve.py) to do so.

```

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
        
```

Run this script with python after replacing HOST and PORT.

```
$ python solve.py
[+] Opening connection to HOST on port PORT: Done
.
.
.
l00s lines of output 
.
.
.
fun() took 3.000000 seconds to execute csictf{h3_7u2n3d_h1m531f_1n70_4_p1ck13}
```

The flag is:
```
csictf{h3_7u2n3d_h1m531f_1n70_4_p1ck13}
```
