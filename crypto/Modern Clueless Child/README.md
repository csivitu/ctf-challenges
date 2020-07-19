# Modern Clueless Child

Author: [SrishtiGohain](https://github.com/SrishtiGohain)

## Description

This is a very simple crypto challenge which uses XOR Encryption.

## Requirements

- Python (2.x)
- Online XOR Encryptor

## Sources

```
"I was surfing the crimson wave and oh my gosh I was totally bugging. I also tried out the lilac hair trend but it didn't work out. 
That's not to say you are any better, you are a snob and a half. But let's get back to the main question here-
Who am I? (You don't know my name)"

Ciphertext= "52f41f58f51f47f57f49f48f5df46f6ef53f43f57f6cf50f6df53f53f40f58f51f6ef42f56f43f41f5ef5cf4e" (hex)
Key="12123"
```

## Exploit
Our goal is to generate the flag, and we know for a fact that it should start with `csictf{`. We also know that the first byte in the hex cipher text is `0x52` = 82 (base 10), and the character 'c' in ascii is 99. Since a key is given, it is useful to attempt to do an XOR, we notice that 
```
82 ^ 99 = 49
```
49 is 1 in ascii, which matches the first character of key!
But when we try the next byte, 0xf4 = 244, with the next character of the flag 's' = 115, we notice that
```
244 ^ 115 = 135
```
Which does not match the next character of the key (2 = 50 in ascii)

We make the crucial observation that to match 's', you would have needed
```
115 ^ 50 = 65
```
65 = 0x41, and we notice its in the cipher text right after the f. We also make the discovery that 'f' is just obfuscation, repeating every three characters in the flag. We remove the Fs (lol) and use XOR to solve the challenge:

Use the [encryption](./Encryptor.py) and [decryption](./Decryptor.py) scripts to find the flag. Try to encrypt and compare a known text segment with the given
ciphertext, like 'csi' or 'csictf{}' (because the flag format is known). Extra characters (here, 'f') are present (at regular intervals of 2) throughout
the ciphertext. Decrypt the ciphertext after eliminating these extra characters to obtain the flag. 

```python
#encryptionScript

input_str = raw_input("Enter the cipher text : ")
key = raw_input("Enter the key for xor-ing : ")
output_str = ""
no_of_itr=len(input_str)


for i in range(no_of_itr):
    current = input_str[i]
    current_key = key[i%len(key)]
    output_str += chr(ord(current) ^ ord(current_key))

final_str=""
for character in output_str:
    final_str+= character.encode('hex')
print final_str
```

```python
#decryptionScript

istr = raw_input("Enter the cipher text : ")
key = raw_input("Enter the key for xor-ing : ")
output_str = ""

input_str = istr.decode('hex')
no_of_itr=len(input_str)
for i in range(no_of_itr):
    current = input_str[i]
    current_key = key[i%len(key)]
    output_str += chr(ord(current) ^ ord(current_key))
print output_str
```
<br />

The flag is:

```
csictf{you_are_a_basic_person}
```
