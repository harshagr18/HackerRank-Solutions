#Problem Link : https://www.hackerrank.com/challenges/string-validators/problem

a = input()
flag1 = False
flag2 = False
flag3 = False
flag4 = False
flag5 = False
for i in a:
    if i.isalnum():
        flag1 = True
    if i.isalpha():
        flag2 = True
    if i.isdigit():
        flag3 = True
    if i.islower():
        flag4 = True
    if i.isupper():
        flag5 = True
print(flag1)
print(flag2)
print(flag3)
print(flag4)
print(flag5)