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