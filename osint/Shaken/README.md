# Flying Places

Author: [parthkgh24](https://github.com/parthkgh24)

## Description
This is an osint challenge.

## Requirements

- None

## Sources
```
I love this watch. It's been with me all over the world, from Istanbul to Shanghai to Macau.I wear it with suits quite a lot. My boss liked it too. I remember wearing it when she died. What is her successor's name?
```


## Exploit

This picture given is a cropped picture of James Bond's watch from Skyfall. The question mentions wearing the watch in Istanbul, Shanghai and Macau. On searching these, the results all show flight tickets but on moving in a few more pages, results for Skyfall start to appear. Even quicker if you put the word movie as part of the search history. The reverse search for the image doesn't give any references to Skyfall, which is supposed to throw people off. However the name of the image, 300 M is the type of watch worn which is an Omega Seamastr 300 M worn in the movie. Once the person wearing the watch is recognized to be James Bond and the movie referenced is Skyfall, searching the boss (M) and her successor are easy to find.

The flag is:

```
csictf{gareth_mallory} 
```

