# In Your Eyes

Author: [SrishtiGohain](https://github.com/SrishtiGohain)

## Description

This is a forensics challenge that also uses Braille encoded text.

## Requirements

- Hidden file extracting software

## Sources

```
" I talk of wondrous things I see,
  You picture purely out of imagination,
  You wonder how your light is spent,
  Days seem bright but you don't know for sure.
  I stand in your place and close my eyes,
  What do I see?"
  (Open your windows to see the secret message)
```

## Exploit

Extract the hidden text file from the picture provided using Steganography software (like Quick Stego). You will see a hex string. Convert this to binary to get the Braille encoded flag.
Each Braille character is representated by six bits (from L to R) except the curly braces which are representated by twelve bits each (in accordance with the Braille format). Convert the Braille characters to normal letters to obtain the flag.

<br />

The flag is:

```
csictf{nowucme}
```
