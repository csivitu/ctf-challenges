# esrom

Authors: [21StWarlock#1598](21StWarlock#1598)

Reverse morse code(audio) to get a combination of 1's and 0's and then reverse that to get hex converstion of the flag

# Requirements

- Python 3
- Morse code decoder
- hex code decoder

Files: flag.wav
## Sources

- [morse.wav](./morse.wav)
```
Decode to get the flag
Hint 1: search for morse code audio decoders by morse code international  - Points 100
Hint 2: look deeper in the file - Points 200
```

## Exploit

You have to convert the audio into morse code and then you will get some hex characters:

```
72 65 76 65 72 73 65 6d 6f 72 73 65
```
which when converted to ascii gives a secret key:

```
reversemorse
```

which when used to extract the flag hidden in the morse code using steghide we get falg.txt which has the floowing text :
```
csictf{7h47_w45_50m3_9o0d_r3v3R51n9}
```

 The flag is: `csictf{7h47_w45_50m3_9o0d_r3v3R51n9}`
