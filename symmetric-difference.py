# Problem Link : https://www.hackerrank.com/challenges/symmetric-difference/problem

N = int(input())
N_list = map(int, input().split(' '))
M = int(input())
M_list = map(int, input().split(' '))

N_set = set(N_list)
M_set = set(M_list)

tmp_set1 = N_set.difference(M_set)
tmp_set2 = M_set.difference(N_set)
result = tmp_set1.union(tmp_set2)
result = sorted(result)

for el in result:
    print(el)