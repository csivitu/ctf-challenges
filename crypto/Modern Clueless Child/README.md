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

The flag-

```
csictf{you_are_a_basic_person}
```
