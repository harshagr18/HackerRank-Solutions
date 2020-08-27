# Problem Link : https://www.hackerrank.com/challenges/merge-the-tools/problem

import textwrap

def merge_the_tools(string, k):
    # your code goes here
    temp = textwrap.wrap(string, k)
    for i in temp:
        t = ""
        for j in i:
            if j in t:
                pass
            else:
                t = t+j
        print(t)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)