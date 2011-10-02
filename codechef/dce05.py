import psyco
psyco.full()
def find_number(n):
	sq=0
	a=1
	while(n>a):
		sq=sq+1
		a=a+2**sq
	return 2**sq
t=int(raw_input())
while(t!=0):
	n=int(raw_input())
	ans=find_number(n)
	print ans 
	t=t-1
