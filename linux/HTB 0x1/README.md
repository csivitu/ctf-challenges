# HTB 0x1

Author: [thebongy](https://github.com/thebongy) and [roerohan](https://github.com/roerohan)

## Description

Hackthebox challenge 1.

## Requirements

- Docker

## Sources

```
I forgot my 'flag.txt' file on the server...
```

## Exploit

When you scan the target using `nmap`, you can see that there's an ftp service running on port `5001`. 

```bash
$ nmap -sC -sV -Pn 34.93.37.238
Starting Nmap 7.80 ( https://nmap.org ) at 2020-07-15 10:58 IST
Nmap scan report for 238.37.93.34.bc.googleusercontent.com (34.93.37.238)
Host is up (0.029s latency).
Not shown: 988 filtered ports
PORT     STATE  SERVICE         VERSION
22/tcp   open   ssh             OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
53/tcp   open   domain          ISC BIND 9.14.10
| dns-nsid: 
|_  bind.version: 9.14.10
5001/tcp open   ftp             vsftpd 3.0.3
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
|_Can't get directory listing: PASV IP 10.160.0.2 is not the same as 34.93.37.238
| ftp-syst: 
|   STAT: 
| FTP server status:
|      Connected to ::ffff:103.242.197.208
|      Logged in as ftp
|      TYPE: ASCII
|      No session bandwidth limit
|      Session timeout in seconds is 300
|      Control connection is plain text
|      Data connections will be plain text
|      At session startup, client count was 1
|      vsFTPd 3.0.3 - secure, fast, stable
|_End of status
7000/tcp closed afs3-fileserver
7001/tcp closed afs3-callback
7002/tcp closed afs3-prserver
7004/tcp closed afs3-kaserver
7007/tcp closed afs3-bos
7019/tcp closed doceri-ctl
7025/tcp closed vmsvc-2
7070/tcp closed realserver
7100/tcp closed font-service
Service Info: OSs: Linux, Unix; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 58.78 seconds
```

Visit `ftp://34.93.37.238:5001` on a browser, and find the flag in the `pub` directory.

<br /> 

The flag is:

```
csictf{4n0nym0u5_ftp_l0g1n}
```