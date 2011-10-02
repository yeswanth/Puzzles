letters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
class stack:
	def __init__(self):
		self.items=[]
	def push(self,item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def isEmpty(self):
		return (self.items==[])


n=int(raw_input())	
a=stack()
while(n!=0):
	ans=''
	st=raw_input()
	for i in st: 
		if i in letters:
			ans=ans+i	
		elif i == '(':
			a.push('(')
		elif i == ')':
			if(len(a.items)!=0):
				b=a.pop()
			while a.isEmpty()!=True and b!='(':
				ans=ans+b
				if(len(a.items)!=0):
					b=a.pop()
		elif i != ' ' :
			a.push(i)
	while a.isEmpty()!=True:
		ans=ans+a.pop()
	print ans 
	n=n-1
	
