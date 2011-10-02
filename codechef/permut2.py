from sys import stdin
count=0
lines=stdin.readlines()
a=int(lines[count])
while(int(lines[count])!=0):
	a=int(lines[count])
	count=count+1
	values=map(int,lines[count].split())
	count=count+1
	ltemp=[0 for i in xrange(a+1)]
	for i in xrange(a):
		ltemp[values[i]]=i+1
	ltemp=ltemp[1:]
	if ltemp==values:
		print 'ambiguous'
	else :
		print 'not ambiguous'
	
