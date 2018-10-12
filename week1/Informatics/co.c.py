n = int(input())
m = int(input())

if m==n:
	print("YES")
if m!=n and m==1:
	print("NO")
if m!=n and n==1:
	print("NO")
if m!=n and n!=1 and m!=1:
	print("YES")