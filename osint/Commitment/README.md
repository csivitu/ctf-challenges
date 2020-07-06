# Commitment
Author: [ashikka](https://github.com/ashikka)

## Description

General github knowledge and Sherlock

## Requirements 

- Github
- Sherlock

## Sources

- [hoshimaseok](https://github.com/hoshimaseok)


```
hoshimaseok is up to no good. Track him down.
```


## Exploit

You need to search all accounts on the internet using the username `hoshimaseok` using the tool [Sherlock](https://github.com/sherlock-project/sherlock). Once you land on the github account, you see there is one repository named `SomethingFishy`. In this repository, on the branch `dev`, there are many folders, full of random code, that doesn't really make any sense. On scouring through the commit history, you stumble across something unsual. The `.gitignore` file has been updated twice. 
<br />

Now, when you open this commit, you find out that the user had mistakenly pushed his `.env` file with the flag and had forgotten to add `.env` to the `.gitignore` file. 
<br />


The flag is:

```
csictf{sc4r3d_0f_c0mm1tm3nt}
```
