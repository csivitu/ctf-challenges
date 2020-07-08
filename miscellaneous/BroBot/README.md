
# BroBot

Authors: [alias-rahil](https://github.com/alias-rahil)

## Description

A code injection challenge!

# Requirements

- Python
- espeak
- Docker

## Sources

- [bot.py](./bot.py)
- [flag.txt](./flag.txt)

## Challenge description to go up on the website.

```
This BoT can speak, can you ask him the flag? https://telegram.me/csictf_brobot/
```

# Exploit

The user will be given the link to a telegram bot which can convert text to voice. The user can get repo link of the bot by using the `/about` command. He will notice a line `fs.write(f"echo '{text}'")` in the code. The exploit is sending `'; cat flag.txt; echo '` to the bot in the `/text2voice` command. The bot will send the flag as voice.
 
The Flag is:
```
csictf{ai_will_take_over_the_world}
```
