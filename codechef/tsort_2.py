import psyco
psyco.full()
t=int(raw_input())
val=[]
for i in range(t):
	val.append(int(raw_input()))
a=sorted(val)
for i in a:
	print i 
