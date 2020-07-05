# Panda
Author: [ashikka](https://github.com/ashikka)

## Description

Steganography and bruteforce.

## Requirements 

- FlexHex
- john (the ripper)

## Sources

- [panda.zip](./panda.zip)


```
I wanted to send this file to AJ1479 but I did not want anyone else to see what's inside it, so I protected it with a pin.
```


## Exploit

You need to bruteforce 4 lettered pin `(2611)` using a tool like `john (the ripper)` to access the zipped file. Then, unzip the file to see two images, one of them distorted. You need to use a tool like `FlexHex` to compare the two images, to find out that the hexadecimal values that are different when concatenated comprise of the flag.

The flag is:

```
csictf{kung_fu_p4nd4}
```
