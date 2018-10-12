a = []

n = int(input())
s = input()

a.append([int(x) for x in s.split()])

for x in range(0 , n):
	if x%2==0:
		print(a[0][x] , end = ' ')