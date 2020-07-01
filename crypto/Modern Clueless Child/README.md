# Modern Clueless Child

Author: [SrishtiGohain](https://github.com/SrishtiGohain)

## Description

This is a very simple crypto challenge which uses XOR Encoding.

## Requirements

- Online XOR Decryptor

## Sources

```
"I was surfing the crimson wave and oh my gosh I was totally bugging. I also tried out the lilac hair trend but it didn't work out. 
That's not to say you are any better, you are a snob and a half. But let's get back to the main question here- Who am I? (You don't know my name)"
Ciphertext= "01160b061603191c0d103d0410003d0703160b063d070b11010d1f" (hex)
Key="bebebebebebebebe"
```

## Exploit

You just have to play around with the ciphertext to realize that adding '-' after every 2 characters and decrypting will easily give you the flag. One way of figuring this out
is to encrypt the flag format (csictf) to see the same hex text in the cipher.
<br />

The flag-

```
csictf{you_are_basic_bitch}
```
