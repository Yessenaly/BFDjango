import sys
n = int(input())
if n%2==1 :
    print("Weird")
    sys.exit()    
if n>=2 and n<=5 :
    print("Not Weird")
    sys.exit()
if n<=20 :
    print("Weird")
    sys.exit()
print("Not Weird")