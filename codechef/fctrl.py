def factorial():
	a=int(raw_input())
	while(a!=0):
		b=int(raw_input())
		ans=find_factors(b)
		print ans 
		a=a-1
	
def find_factors(b):
	a=5
	ans=0
	while(b/a!=0):
		ans=ans+(b/a)
		a=a*5
	return ans
factorial()

		
	
