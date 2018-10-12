import sys

x = int(input())
y = int(input())
z = int(input())

n = int(input())

if x==0 and y==0 and z==0 and n==0:
	print("[]")
	sys.exit()

s=""

s+="["
for i in range(0 , x+1):
	for j in range(0 , y+1):
		for k in range(0 , z+1):
			if i+j+k!=n:
				s+="["+str(i)+", "+str(j)+", "+str(k)+"], "
s = s[:-2]
s+="]"
print(s)