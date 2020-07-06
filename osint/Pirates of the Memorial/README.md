# Pirates of the Memorial

Author: [roerohan](https://github.com/roerohan)

## Description

An OSINT challenge where you scour the internet to find the owner of this image.

## Requirements

- Internet

## Sources

- [storm.jpeg](./storm.jpeg)

```
The original photographer of this picture commented the flag on his post. Find the flag.
```

## Exploit

When you search the image on `Google`, you find out that it's a picture of `Victoria Memorial`. Then you see some tweets with that picture by `Rishi Bargee`. When you open it, you see there's a comment asking who took this picture, and someone has replied that it was taken by `Arunopal Banerjee`. When you search him up, you find his `Facebook` and `Instagram`, etc. You can see that he's mostly active and posting on his instagram channel.
<br />

Now, when you search through his channel, you find the same picture, in [this](https://www.instagram.com/p/B3oKrLQgpko/?utm_source=ig_web_copy_link) post. Scrolling through the comments, you find the flag.
<br />

The flag is:

```
csictf{pl4g14r1sm_1s_b4d}
```