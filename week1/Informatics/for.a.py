a = int(input())
b = int(input())

for x in range (a , b):
	if x%2==0:
		print(str(x)+" ", end = '')
if b%2==0:
	print(b)