#Problem Link = https://www.hackerrank.com/challenges/python-lists/problem

u = int(input())
final = []
for o in range(u):
    a = input()
    if "insert" in a:
        a = a.replace("insert ","")
        i,e = list(map(int, a.split(" ")))
        final.insert(i,e)
    if "print" in a:
        print(final)
    if "remove" in a:
        a = a.replace("remove ","")
        final.remove(int(a))
    if "append" in a:
        a = a.replace("append ","")
        final.append(int(a))
    if "sort" in a:
        final.sort()
    if "pop" in a:
        final.pop()
    if "reverse" in a:
        final.reverse()