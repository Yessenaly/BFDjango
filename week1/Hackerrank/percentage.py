n = int(input())
student_marks = {}
for x in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
ans = 0
for x in range( 0 , len(student_marks[query_name])):
    ans+=student_marks[query_name][x]
ans/=3.0
print('%.2f' % ans)