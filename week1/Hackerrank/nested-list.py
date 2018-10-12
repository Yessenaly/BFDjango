n = int(input())
a = []
s = []
ans = []

for i in range(0 , n):
    s.append(input())
    a.append(float(input()))
mini = 1000
for i in range(0 , n):
    if a[i]<mini:
        mini=a[i]
mini2 = 1000
for i in range(0 , n):
    if a[i]<mini2 and a[i]!=mini:
        mini2=a[i]
for i in range(0 , n):
    if a[i]==mini2:
        ans.append(s[i])
ans.sort()
for i in range(0 , len(ans)):
	print(ans[i])
