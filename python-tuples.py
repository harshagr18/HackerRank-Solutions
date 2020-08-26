#Problem Link = https://www.hackerrank.com/challenges/python-tuples/problem

u = int(input())
a = tuple(map(int,input().split()))
print(hash(a))