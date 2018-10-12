import math

n = int(input())
s = 0

for x in range(1 , int(math.sqrt(n))+1):
	if(n%x==0):
		s+=1
if n==(int(math.sqrt(float(n))))*(int(math.sqrt(float(n)))):		
	print(s+s-1)
else:
	print(s+s)