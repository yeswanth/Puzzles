x,y=raw_input().split()
x=float(x)
y=float(y)
if(x+0.5>y):
	print "%0.2f" %y
elif(x%5!=0):
	print "%0.2f" %y
else:
	z=y-x-0.5
	print "%0.2f" %z
