# No 'DIS'tractions

Author: [Shiv10](https://github.com/Shiv10)

## Description

This challenge is integrated with the discord bot made for the csictf 2020. The user will have to send a '.flag' command to the bot and the bot will send them the flag.

## Requirements

- Discord

## Sources



```
I see all, I read all, but I shall not speak until I am asked to. Ask me, and thou shall recieve.


Hint 1: It's all in the name - Points 100
Hint 2: Siri and Alexa might be smarter than me, but they won't tell you the answer for this question, I will. - Points 200
```

## Exploit

<!-- Much more detailed description than the following. -->
The challenge requires the user to figure out that they have to send a private message to the bot in order to recieve the flag. Texting the bot on any of the text channels will not work and the bot will send the flag only when the user messages the bot privately. If you message the bot on an of the text channels, you get a response which hints you towards messaging the bot personally. 
<br />

<br />

The flag is:

```
csictf{m0r3_huMaN_than_Y0u}
```