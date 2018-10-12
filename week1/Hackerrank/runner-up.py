n = int(input())
a = []
s = input()

a.append([int(x) for x in s.split()])
maxi=-1000
for x in range(0 , n):
	if a[0][x]>maxi:
		maxi=a[0][x]
maxi2=-1000
for x in range(0 , n):
	if a[0][x]>maxi2 and a[0][x]!=maxi:
		maxi2=a[0][x]
print(maxi2)