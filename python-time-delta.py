# Problem Link : https://www.hackerrank.com/challenges/python-time-delta/problem

from datetime import datetime

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s1 = input()
        s2 = input()
        t1 = datetime.strptime(s1, "%a %d %b %Y %H:%M:%S %z")
        t2 = datetime.strptime(s2, "%a %d %b %Y %H:%M:%S %z")
        print(abs(int((t1-t2).total_seconds())))