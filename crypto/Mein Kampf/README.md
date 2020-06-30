# Mein Kampf

Author: [AJ1479](https://github.com/AJ1479)

## Description

This is a simple crypto challenge which uses the Enigma Cipher.

## Requirements

- Online Enigma Decoder

## Sources

```
"We have intercepted the enemy's communications, but unfortunately, some data was corrupted during transmission. Can you recover the message?"  
M4 
UKW $
Gamma 2 4 
$ 5 9 
$ 14 3 
$ 5 20 
fv cd hu ik es op yl wq jm

Ciphertext: zkrtwvvvnrkulxhoywoj
(Words in the flag are separated by underscores)
```

## Exploit

The model, reflector, and rotors and their positions, of the machine have been given to the players. You just have to use the online [Enigma decoder](https://cryptii.com/pipes/enigma-machine). You have to use brute force to find out the reflector type and the missing rotors, which you'll find out to be B, I, IV, and VII respectively. 
<br /> 

The flag is:

```
csictf{no_shit_sherlock}
```