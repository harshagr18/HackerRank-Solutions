# Problem Link : https://www.hackerrank.com/challenges/find-a-string/problem

def count_substring(s,d):
    f=1
    ans=0
    l=len(s)
    for i in range(0,l):
        if s[i]==d[0] and i+len(d)<=l:
            for j in range(0,len(d)):
                if s[i+j]!=d[j]:
                    break
                if j==len(d)-1:
                    ans+=1
    return(ans)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)