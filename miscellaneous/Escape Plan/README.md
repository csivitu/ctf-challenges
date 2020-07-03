
# Challenge name

Authors: [Rahil](https://github.com/alias-rahil)

## Description

Another pyjail challenge with a little twist at the end to find the flag.

# Requirements

- Python
- Docker

## Sources

- [crypto.py](./src/crypto.py)
- [dotgit/](./src/dotgit/)
- [start.sh](./src/start.sh)

## Challenge description to go up on the website.

I found a CLI tool to solve cryptography, they say it's pretty secure!

# Exploit

It is a python file running on a netcat listener which can encode/decode crypto ciphers. It uses eval function which can be easily exploited to gain a shell access. The user will then find a `.git` folder and if he checks older commits of the repo, he will find a `.env` file which was deleted later containing the flag.
 
## The Flag:
csictf{2077m4y32_h45_35c4p3d}
