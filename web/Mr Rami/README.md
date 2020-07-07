# Mr. Rami

Author: [roerohan](https://github.com/roerohan)

## Description

This is a simple `robots.txt` challenge.

## Requirements

- Knowledge of `robots.txt`.

## Sources

- [index.html](./index.html)
- [flag.txt](./flag.txt)
- [robots.txt](./robots.txt)
- [server.py](./server.py)

```
"People who get violent get that way because they can’t communicate."
```

## Exploit

When you google the challenge description, you find out that the quote is from Mr. Robot. This indicates that the user might want to check out the `robots.txt` for the website.
<br />

When you open the website, it serves the `index.html` file, which has content written about `Brobot`, again trying to put across `robots.txt`. When you visit `robots.txt`, you see:

```
# Hey there, you're not a robot, yet I see you sniffing through this file.
# SEO you later!
# Now get off my lawn.

Disallow: /fade/to/black
```

When you visit the disallowed route, you get the flag!
<br />

The flag is:

```
csictf{br0b0t_1s_pr3tty_c00l_1_th1nk}
```
