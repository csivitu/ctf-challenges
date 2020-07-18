# Scrambled Eggs

Author: [AJ1479](https://github.com/AJ1479)

## Description

This is a reversing challenge.

## Requirements

- Python

## Sources

- [scrambledeggs.py](./scrambledeggs.py)
- [scrambledeggs.txt](./scrambledeggs.txt)

```
I like my eggs sunny side up, but I ended up scrambling them.
```

## Exploit

This challenge uses random values but the text is simply getting rotated by these. The solution script is specified in [scrambledeggssolve.py](./scrambledeggssolve.py).

As the last step is rotating the flag by a random number and then swapping values, you'll have to work with 28 different texts, rotated by all values from 0 to 27.

Random values from the map are basically getting appended to the front of the key2 and each letter getting appended is just increasing the ascii value of the corresponding letter of the key by it's alphabet number. You need to reverse this to get one key.

You can see that the keys are getting randomly shuffled too, so you might have to try twice with each value to figure out which key is actually `key1` and which one is `key2`. You'll probably figure that out soon enough, as key2 is key1 encrypted with the `enc2` encryption twice. You can decrypt it to find out the right key number. 

Reverse the swapping and the right text string of the 28 options will be the one which will give you the flag but just rotated by some value. You can either try looking at the strings you get on decryption and figure out that it's a rotated flag, or you can rotate each of the 28 strings you get 28 times and look for `csictf`.

The flag is:

```
csictf{all_the_kings_horses}
```