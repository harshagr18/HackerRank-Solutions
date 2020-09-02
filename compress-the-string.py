# Problem Link : https://www.hackerrank.com/challenges/compress-the-string/problem

x=input()
x=x+'.'
count=1
for i in range(0,len(x)-1):
    if(x[i]==x[i+1]):
        count+=1
    else:
        print((count,int(x[i])),end=" ")
        count=1