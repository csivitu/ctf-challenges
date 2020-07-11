# Just Stalin for Time

Author: [parthkgh24](https://github.com/parthkgh24)

## Description
This is an osint challenge, that has a WWII theme.
## Requirements

- None

## Sources

In this question, we have a webpage, where on the first half, there’s a video with a press to make me fall button, which would make the video fall to the bottom of the screen. On the second half, theres a quote that says “Remove a letter, it’s now a slur, remove another letter, the opposite of a blur Sometimes we are captured and hung” (in red if not visible in the README) given at the top. Below it, a picture of Dwayne Johnson and David Beckham with the words Looking for another one below it. The question is: Who took it? What was taken? Note: The format of the flag is csictf{answer1_answer2}

## Challenge description to go up on the website
Hint: “Wkh yrlfh ri wkh shrsoh”- Julius Caesar
5 months, 73 years to the day. 

## Exploit

The video is a 26 second clip from the song Berlin Song https://www.youtube.com/watch?v=JhfwI3gIkzA, from 00:19 to 00:45 seconds, which signifies the time 19-45 or 1945. The falling down signifies the fall of Berlin which happened in 1945 when the Soviets stormed the city and essentially ended WWII. The quote on the right refers to a flag( remove l to get fag and remove f to get lag. Flags can be hung up or captured ctf lol) The David Beckham Dwayne Johnson photo is there because they share the same birthday May 2, which is the same date that Berlin actually fell and the flag of the Soviet Union was put up in Berlin. The caption Looking for another means either looking for another thing that happened on May 2 or looking for another picture related to the thing. The picture that is being referenced is the Rise of the flag in Reichstag which was taken on May 2 1945. So the thing about this picture is that the picture is doctored. The most popular image, the one that is known today, has the watch on one of the wrists removed and the contrast is changed. So who took it refers to the photographer Yevgeny Khaldei, and what was taken is the watch. 

The flag is:

```
csictf{yevgeny_khaldei_watch} 
```

