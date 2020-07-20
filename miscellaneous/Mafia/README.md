# Mafia

Author: [harsoh](https://github.com/harsoh)

## Description

Challenge based on randomized algorithms and binary search.

## Requirements

- Docker: [Dockerfile](./Dockerfile)

## Sources

- [prob.pdf](./prob.pdf)
- [ques.cpp](./ques.cpp)
- [ans.py](./ans.py)

```
The CTF Mafia wants to remove the competition (i.e.you) to again have monopoly over flags. Bribe the Mafia to get away unscathed and with the flag. 

```

## Exploit

The question boils down to finding the max element in a list of 300 random integers with atmost 1000 queries. The queries can determine whether the element at 
some (position) is greater, lesser or equal to some (value). <br /> 
A naive solution is to try to find the value of every element using binary search but binary search will need around log2(1000000)~20 queries per element which is much 
more than the number of queries we have. <br /> 
A key observation is that we don't need to binary search the value of an element every time but rather only when its greater than the current maximum, because otherwise it
can't be the max element and is of no use to us. It can be proven that when we traverse through an array of size n in random order, we will encounter a number greater than the
current maximum ~log2(n) times. Read more on Expectation of Value to know more about this claim.<br /> 
Thus we do atleast one query on each element to determine whether its greater than current maximum and log2(1000000) queires on log2(n) elements to determine their value.
Thus doing a total of n + log2(1000000)*log2(n) queries which for n=300 comes around 464 which is much less than the 1000 queries bound given.

```
import sys

curr_max=1
for i in range(1,301):
	print(1,i,curr_max)
	sys.stdout.flush()
	ch=input()
	if(ch=='G'):
		low = curr_max+1
		high = 1000000
		mid = 0
  
		while(low<=high): 
			mid = (high + low) // 2
			print(1,i,mid)
			sys.stdout.flush()
			ch2=input()
			if(ch2=='G'): 
				low = mid + 1
			elif(ch2=='L'): 
				high = mid - 1
			else: 
				if(mid>curr_max):
					curr_max=mid
				break

print(2,curr_max)
```

<br /> 

The flag is:

```
csictf{y0u_ar5_t8e_k!ng_0f_rAnd0mne55}
```
