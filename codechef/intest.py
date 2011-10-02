n,k=raw_input().split()
n=int(n)
k=int(k)
ans=0
while(n!=0):
	a=int(raw_input())
	if(a%k==0):
		ans=ans+1
	n=n-1
print ans
	
