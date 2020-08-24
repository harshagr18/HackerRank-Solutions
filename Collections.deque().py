#Problem Link = https://www.hackerrank.com/challenges/py-collections-deque/problem
from collections import deque
d = deque()
final = ""
u = int(input())
for o in range(u):
    a = input()
    if "append" in a and "appendleft" not in a:
        a = a.replace("append ","")
        d.append(int(a))
    elif "appendleft" in a:
        a = a.replace("appendleft ","")
        d.appendleft(int(a))
    elif "pop" in a and "popleft" not in a:
        d.pop()
    else:
        d.popleft()
    
for i in d:
    final = final + str(i) + " "
print(final)