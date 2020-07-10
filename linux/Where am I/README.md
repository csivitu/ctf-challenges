
# Where am I

Authors: [alias-rahil](https://github.com/alias-rahil)

## Description

A linux chroot jail challenge.

# Requirements

- Docker

## Sources

- None

```
Something is not right? I feel like I am in a prison!

Hint 1: My friend once escaped a jail using ssh, I wonder how?
```

# Exploit

It is a simple chroot escape challenge. The user will be given a shell where he can run commands. He should be able to notice that there there is a pair of ssh keys present inside `/root/.ssh` folder. He will then use the command `ssh -i /root/.ssh/id_rsa -o StrictHostKeyChecking=no root@localhost` to get the flag.

The Flag is:
```
csictf{n1c3_d093_w0w_5uch_55h}
```
