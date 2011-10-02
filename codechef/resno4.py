from sys import stdin
lines= stdin.readlines()
t=int(lines[0])
count=1
for x in range(t):
	player=0
	n=int(lines[count])
	count=count+1
	stones=map(int,lines[count].split())
	count=count+1
	ans = 0
	for i in range(len(stones)):
		ans=ans+stones[i]/(i+1)
	if ans%2 == 0 :
		print 'BOB'
	else: 
		print 'ALICE'
		
	 
