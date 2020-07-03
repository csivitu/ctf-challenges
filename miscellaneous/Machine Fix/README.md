# Challenge Name

Author: [Soham](https://github.com/harsoh)

## Description

To help fix the machine, download the PDF.

Hint 1: The machines act like ternary numbers.

Hint 2: Think of the contribution of each machine separately.

## Requirements

- Docker: [Dockerfile](./Dockerfile)

## Sources

- [sol.py](./sol.py)
- [prob.pdf](./prob.pdf)

## Exploit

The problem is a complicated way of saying - Given a positive integer n, find the sum of number of positions with different bits between consecutive ternary numbers from 0 to n.
The answer could have been brute-forced but the number is of the order 10^30 so it is not possible. Rather understanding how bits work in any general base helps. <br />
For base-3 or ternary numbers, the LSB changes whenever we increase a number by 1, the 2nd last bit changes whenever we increase a number by 3, 3rd last bit whenever we increase
by 9 and so on... <br />
So we calculate contribution of each bit and sum them up to get the answer. The contribution of the k(th) last bit can be calculated by ( n//( 3^(k-1) ) ) where // represents 
integer division. This is because the k(th) last bit changes whenever we increase by 3^(k-1) and we are going from 0 (all machines empty) to n so total increment by n.
<br />

The flag is:
csictf{785539772602034710213927792950}
