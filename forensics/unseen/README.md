# unseen

Authors: [21StWarlock#1598](21StWarlock#1598)

Using LSB we find the key to the steghidden file inside the morse.wav which contains a whitespcace code which prints the flag .
# Requirements

- Python 3
- Morse code decoder
- whitespace interpreter 
- steghide

Files: 
- morse.wav
- nyc.jpg

## Sources

- [morse.wav](./morse.wav)
- [nyc.jpg](./nyc.jpg)

```
With his dying breath, Prof. Ter Stegen hands us an image and a recording. He tells us that the image is least significant, but is a numerical key to the recording and the recording hides the answer. It may seem as though it's all for nothing, but trust me it's not.
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


when we first look at `Flag.txt` it seems empty but it is filled woth tabs and spaces, using whitespace interpreter when we run the `flag.txt` we get the flag : 
```
csictf{7h47_15_h0w_y0u_c4n_83c0m3_1nv151813}
```

The flag is: 
```
csictf{7h47_15_h0w_y0u_c4n_83c0m3_1nv151813}
```
