#Problem Link = https://www.hackerrank.com/challenges/finding-the-percentage/problem

marks = {}
sum = 0.00
u = int(input())
for o in range(u):
    temp = list(map(str,input().split()))
    marks[temp[0]] = temp[1:]
a = input()
final = marks[a]
for i in final:
    sum = sum + float(i)
ans = sum/len(final)
ans = "{:.2f}".format(ans)
print(ans)