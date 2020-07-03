n=int(input())
x=1
ans=0
while(x<=n):
	ans+=n//x
	x*=3
print(ans)