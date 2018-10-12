def pow(a , b):
	return (a+b)%2

s = input()

a = []
a.append([int(x) for x in s.split()])

print(pow(a[0][0] , a[0][1]))
# print(float(a[0][0]**a[0][1]))
