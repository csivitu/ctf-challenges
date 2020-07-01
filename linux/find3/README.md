# Challenge Name - Find2

Author: [Pragati1610](https://github.com/pragati1610)

## Description

Reach the final flag, so don't blow your horns too fast :
enter the challenge through ~hosted-site~ at port XXXX

## What is it :
-  A course of 2 challenges using the linux command line tools 

## Exploit :
- ssh ~hosted-site~ -p XXXX
Sentences can play games, so do their lengths, look carefully for your flag or make amends!
> root$ ls -a
> dir1 dir2 dir3 dir4 dir11 dir12 dir13 dir14 
> root$ 

[can brute force]
[or run command > root$ find ./ -size 91c]
[or run command >root$ grep -r csictf *]

> /dir12/ file3.txt

Contents of file.txt :(the fullstop is the 91st byte)
csictf{st4rt_w1th_0n3_3nd_w1th_3} challenge 2 is at ~some-site~ port XXXX                 .

> exit

- ssh ~some-site~ port XXXX
Stuck wondering what to do? No similar files contain the flag, why not change the view?

> C:\ dir
file1.txt file2.txt file3.txt file4.txt file5.txt file6.txt 
> C:\ fc /a file1.txt file2.txt [compare each of them - 5 of them are identical, one contains the flag]

(for ex :file1 and file2 contain junk data except 1 string which is in file1 and not in file2)

> file1
...s0m3_junk_d4t4s0m3_junk_d4t4s0m3_junk_d4t41_4m_h3h3_y0u_jusT_F0unD_m3s0m3_junk_d4t4s0m3_junk_d4t4s0m3_junk_d4t4s0m3_junk_d4t4s0m3_junk_d4t4s0m3_junk_d4t4...
file2
...s0m3_junk_d4t4s0m3_junk_d4t4s0m3_junk_d4t4s0m3_junk_d4t4s0m3_junk_d4t4s0m3_junk_d4t4s0m3_junk_d4t4s0m3_junk_d4t4s0m3_junk_d4t4...


## Requirements

- Docker: [Dockerfile](./Dockerfile)

## Sources

- [sample.py](./sample.py)
- [sample.txt](./sample.txt)
