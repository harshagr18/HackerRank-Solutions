# Problem Link : https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    for i in range(1,number+1):
        oc = oct(i)[2:]
        he = hex(i)[2:]
        bi = bin(i)[2:]
        print(str(i)+" "+str(oc)+" "+str(he)+" "+str(bi))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)