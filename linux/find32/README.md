# find32

Author: [Pragati1610](https://github.com/Pragati1610)

## Description

This is a linux based finding challenge.

## Sources

```
I should have really named my files better. I thought I've hidden the flag, now I can't find it myself.
(Wrap your flag in csictf{})

ssh user1@chall.csivit.com -p 30630
Password is find32
```

## Exploit

Login to the server using `ssh`.

```bash
$ ssh user1@chall.csivit.com -p 30630
```

You see a lot of folders. Try to grep `csictf` in them.

```bash
$ grep -irs csictf
........csictf{not_the_flag}{user2:AAE976A5232713355D58584CFE5A5}.......
```

This shows the password for `user2`.

```bash
$ su user2
Password: 
user2@1d864575646e:/user1$ cd /user2
user2@1d864575646e:~$ 
```

Now, you see some text files, but you don't find anything when you grep `csictf`. You can see that all the files are same. Or are they?

```bash
user2@1d864575646e:~$ diff adgsfdgasf.d sadsas.tx 
42391a42392
> th15_15_unu5u41
```

When you run `diff` on pairs of files, you see they're same, expcept `sadsas.tx`. Wrap this text in `csictf{}` and get the flag.

The flag is:
```
csictf{th15_15_unu5u41}
```