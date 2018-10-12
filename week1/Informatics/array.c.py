a = []

n = int(input())
s = input()

ans=0

a.append([int(x) for x in s.split()])

for x in range(0 , n):
	if a[0][x]>0:
		ans+=1
print(ans)