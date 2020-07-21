# Secret Society

Author: [harsoh](https://github.com/harsoh)

## Description

Challenge based on buffer overflow exploit.

## Requirements

- Docker: [Dockerfile](./Dockerfile)

## Sources

- [prob.c](./prob.c)

```
Wanna enter the Secret Society? Well you have to find the secret code first!

```

## Exploit

The question asks us for the secret phrase and that is the only thing we can enter. So to get the flag we have to exploit it somehow. The first thing to notice is that the secret_phrase buffer comes just after the flag buffer. Noticing that the strcat function can cause an overflow leads to the answer. We need to do a stack flood, i.e. just input alot of random bits and the strcat function would append some string to to the secret_phrase buffer and push the null byte to the flag buffer and thus printing out the secret phrase along with the flag.

```
$ python2 -c "print 'a'*1000" | ./Secret Society
```

<br /> 

The flag is:

```
csivit{Bu!!er_e3pl01ts_ar5_5asy}
```
