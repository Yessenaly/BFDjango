import math

a = int(input())
b = int(input())

for x in range(a , b+1):
	e = math.sqrt(float(x))
	e = int(e)
	e = e*e
	if e==x:
		print(x , end=' ')