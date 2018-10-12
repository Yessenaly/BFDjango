a = []

n = int(input())
s = input()

ans=0

a.append([int(x) for x in s.split()])

for x in range(1 , n-1):
	if a[0][x]>a[0][x-1] and a[0][x]>a[0][x+1]:
		ans+=1
print(ans)