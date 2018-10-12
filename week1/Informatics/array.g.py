a = []

n = int(input())
s = input()

ans=0

a.append([int(x) for x in s.split()])
a[0].reverse()

for x in range(0 , n):
	print(a[0][x] , end=' ')