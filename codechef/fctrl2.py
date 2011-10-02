def factorial(a):
	ans=1
	while(a!=1):
		ans=ans*a
		a=a-1
	return ans
		
	
n=int(raw_input())
while(n!=0):
	a=int(raw_input())
	print factorial(a)
	n=n-1


