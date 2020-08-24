#Problem Link - https://www.hackerrank.com/challenges/list-comprehensions/problem


a = int(input())
b = int(input())
c = int(input())
n = int(input())

i = 0
j = 0
k = 0
final = []

while(i<=a):
    j = 0
    while(j<=b):
        k = 0
        while(k<=c):
            if i+j+k != n:
                final.append([i,j,k])
            k = k+1
        j = j+1
    i = i+1
print(final)