# Problem Link : https://www.hackerrank.com/challenges/no-idea/problem

n,m = list(map(int, input().split()))
mainlist = list(map(int,input().split()))
happylist = set(map(int,input().split()))
sadlist = set(map(int,input().split()))
score = 0
for i in mainlist:
    if i in happylist:
        score = score + 1
    elif i in sadlist:
        score = score - 1
print(score)