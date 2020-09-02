# Problem Link : https://www.hackerrank.com/challenges/most-commons/problem

arr=[]
s=input()
lenn=len(s)
s1=sorted(s)
arr[:27]=[0] * 27
for i in s1:
    arr[ord(i)-97]+=1
maxx=-1
pos=-1
for j in range(3):
    for i in range(27):
        if maxx< arr[i]:
            maxx=arr[i]
            pos=i
    print(chr(pos+97),maxx)
    maxx=-1
    arr[pos]=-2
    pos=-1