# unseen

Authors: [21StWarlock#1598](21StWarlock#1598)

Using LSB we find the key to the steghidden file inside the morse.wav which contains a whitespcace code which prints the flag .
# Requirements

- Python 3
- Morse code decoder
- whitespace interpriter 
- steghide

Files: 
- morse.wav
- nyc.jpg

## Sources

- [morse.wav](./morse.wav)
- [nyc.jpg](./nyc.jpg)

```
Decode to get the flag
Hint 1: https://incoherency.co.uk/image-steganography/  - Points 100
Hint 2: steghide - Points 200
```

## Exploit

You have to find the hidden code in `[nyc.jpg](./nyc.jpg)` by using lsb steganography :
```
When you visit https://incoherency.co.uk/image-steganography/ and do extract image, at lsb of value 1 bit you get a new image with some numbers  
```

and the password you get is :
```
42845193
```
then when you apply steghide `steghide extract -sf morse.wav` you get flag.txt


[flag.txt](./flag.txt)


when we first look at `Flag.txt` it seems empty but it is filled woth tabs and spaces , using whitespace interpriter when we run the `flag.txt` we get the flag : 
```
csictf{7h47_15_h0w_y0u_c4n_83c0m3_1nv151813}
```

 The flag is: `csictf{7h47_15_h0w_y0u_c4n_83c0m3_1nv151813}`
