#Problem Link : https://www.hackerrank.com/challenges/python-string-split-and-join/problem

def split_and_join(line):
    a = list(map(str,line.split()))
    new = ""
    for i in a:
        new = new + i + "-"
    return(new[:-1])

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)