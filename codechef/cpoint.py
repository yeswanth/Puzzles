import math
from sys import stdin
def distance(x1,y1,x2,y2):
	t1=math.pow(x1-x2,2)
	t2=math.pow(y1-y2,2)
	ans= math.sqrt(t1+t2)
	return ans 
def listdistance(lx,ly,x1,x2):
	dis=0
	for i in range(len(lx)):
		dis=dis+distance(lx[i],ly[i],x1,x2)
	return dis	
def tsearch(lx,ly,x,i,j,mn):
	m1=int(i+(j-i)/3)
	m2=int(j-(j-i)/3)
	if ly[m1]>ly[m2]:
		a=listdist(lx,ly,x,ly[m1])
		b=listdist(lx,ly,x,ly[m2])
		if a>b:
			if b<mn:
				mn=b
			tsearch(lx,ly,m1+1,j,mx)
		else:
			if a<mn:
				mn=a
			tsearch(lx,ly,i,m2-1,a)
	else :
		return 	mn
lines=stdin.readlines()
count=0
while(lines[count]!=0):
	t=lines[count]
	count = count + 1	
	xp=[]
	yp=[]
	for i in range(t):
		x,y=lines[count].split
		x=int(x)
		y=int(y)
		xp.append(x)
		yp.append(y)
	ymin=min(yp)
	ymax=max(yp)
	tsearch(xp,yp,ymin,ymax,0)
	
