# HTB 0x6

Author: [thebongy](https://github.com/thebongy) and [roerohan](https://github.com/roerohan)

## Description

Hackthebox challenge 6.

## Requirements

- Docker

## Sources

```
Server is at 34.93.215.188.
```

## Exploit

You need to log in to the server using [HTB 0x2](../HTB%200x2), then you can check out the source file in `/home/administrator/website/models/db.js` to get this flag. (You can really just `grep` all flags btw XD) You also get the mongo URL which you'll need in [HTB 0x4](../HTB%200x4).

The flag is:

```
csictf{exp0s3d_sec23ts}
```