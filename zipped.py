#Problem Link - https://www.hackerrank.com/challenges/zipped/problem

c=input().split()
a=int(c[0])
b=int(c[1])
temp=[]
num=[]
for i in range(b):
    temp=input().split()
    num.append([float(item) for item in temp])
for j in range(a):
    sum1=0
    for i in range(b):
        sum1=sum1+num[i][j]
    print(sum1/b)
