# Problem Link : https://www.hackerrank.com/challenges/word-order/problem

from collections import OrderedDict

d=OrderedDict()
n=int(input())
for i in range(n):
    s=input()
    if s in d.keys():
        d[s]+=1
    else:
        d[s]=1
print(len(d.keys()))
print(' '.join([str(d[k]) for k in d.keys()]))