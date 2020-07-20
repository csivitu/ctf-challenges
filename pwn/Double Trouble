# Double Trouble
Author: [harsoh](https://github.com/harsoh)

## Description

Challenge based on fast bin double free exploitation.

## Requirements

- Docker: [Dockerfile](./Dockerfile)

## Sources

- [prob.c](./prob.c)

```
The trouble is now double, use it to your advantage to get the flag.

```

## Exploit

The question free's the a pointer twice and the malloc size of bytes is just 10 bytes which falls in fastbin range, this gives us a hint that fast bin double free exploit can
be used. The pointer are freed in the order a->b->a thus when d,e,f are allocated bytes using malloc, d and f pointer get the same memory address. The program takes value to
be stored at d as input and checks whether value stored at f minus 2069 is 40000 or not. Since both d and f have same memory address so both will have same value, 
thus all you need to do is enter 42069 as input.

```
$ python2 -c "print 42069" | ./double-trouble
```

<br /> 

The flag is:

```
csivit{y0u_g0!_fa5t_b!n5}
```
