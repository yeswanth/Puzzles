from sys import stdin
import math
lines=stdin.readlines()
rounds=int(lines[0])
player=0
lead=0
p1=0
p2=0
count = 0 
for  i in range(1,rounds+1):
	a,b=lines[i].split()
	a=int(a)
	b=int(b)
	p1=p1+a
	p2=p2+b
	tmpLead=math.fabs(p1-p2)
	if p1 > p2:
		player = 1
	else :
		player = 2
	if tmpLead > lead:
		lead =  tmpLead
		topPlayer = player
print "%d %d"%(topPlayer,lead)
