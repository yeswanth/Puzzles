
from sys import stdin

t = int(stdin.readline())

h = [int(stdin.readline()) for val in xrange(t)]
h.sort()

for i in h: print i
