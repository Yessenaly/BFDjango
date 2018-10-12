def pow(a , b):
	if b==0:
		return 1
	return a*pow(a , b-1)

s = input()

a = []
a.append([float(x) for x in s.split()])

print(float(pow(a[0][0] , a[0][1])))
# print(float(a[0][0]**a[0][1]))
