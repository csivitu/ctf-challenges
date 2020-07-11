# Archenemy

Author: [roerohan](https://github.com/roerohan)

## Description

Steganography and bruteforce.

## Requirements

- steghide
- john (the ripper)

## Sources

- [arched.png](./arched.png)

```
John likes Arch Linux. What is he hiding?
```

## Exploit

First, use `steghide` to extract the zip hidden in the `arched.png` file (which btw, is a jpg file), with a blank password. If you check the comment in the zip using `zipnote`, it shows `We will, we will, ROCKYOU!`. This is a hint that you have to use `rockyou.txt` to bruteforce the password for the zip.
<br />

First, we convert the zip to a format readable by John The Ripper using `zip2john`.

```bash
$ zip2john flag.zip > flag
ver 2.0 efh 5455 efh 7875 flag.zip/meme.jpg PKZIP Encr: 2b chk, TS_chk, cmplen=27553, decmplen=27752, crc=8F2C73A9
```

Then use `john` with `rockyou.txt`.

```bash
john --wordlist="rockyou.txt" flag
```

This shows you the password `kathmandu`. You get an image file `meme.jpg`, open it to see the flag.
<br />

The flag is:

```
csictf{1_h0pe_y0u_don't_s33_m3_here}
```