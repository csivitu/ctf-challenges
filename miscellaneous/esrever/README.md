
# esrom

Authors: [21StWarlock#1598](21StWarlock#1598)

Reverse morse code(audio) to get a combination of 1's and 0's and then reverse that to get hex converstion of the flag

# Requirements

- Python 3
- Morse code decoder
-   hex code decoder

Files: flag.mp4
```
# Exploitation

 The target in this challenge is to reverse this clip to find the flag .

```
## Sources

- [flag.mp4](./flag.mp4)
```
Decode to get the flag
Hint 1: decode the morse code  - Points 100
Hint 2: search play store for morse code audio decoders - Points 200
```

## Exploit

You have to convert the audio into morse code and then you will get some hex characters which when converted to ascii gives the flag


 The flag is:
```
csictf{7h47_w45_50m3_9o0d_r3v3R51n9}
```
