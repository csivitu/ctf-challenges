# Lo Scampo

Author: [SrishtiGohain](https:github.com/SrishtiGohain)

## Description

This is a simple OSINT challenge.

## Requirements

- none

## Sources

```
Malcolm X took Broiestevane to a Day of the Dead themed party but she never returned. Her only friends, Mr Bean and the Pink Panther realised that she was missing when she didn't show up for an exam. Broistevane liked posting pictures, where was the party held?
(Don't forget to wrap your answer in csictf{})
```

## Exploit

Go to Mr Bean's Instagram account. Go through the posts until you come across [this](https://www.instagram.com/p/CBBAgC9ohzT/), a video of Mr Bean and the Pink Panther giving an exam. In the comments section of this post, you'll find people asking if Mr Brean has found Broiestevane yet, with links to her account. Go to her [account](https://www.instagram.com/broiestevane/?hl=en), you'll see that her final posts are from a party (apparently). In her bio, there is a [link](https://www.instagram.com/p/B3pJE1CgMvI/) to the Day of the Dead party held at The Liberty Hotel.

The flag is:
```
csictf{thelibertyhotel}
```