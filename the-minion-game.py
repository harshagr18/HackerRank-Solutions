# Problem Link : https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(S):
    s=0
    k=0
    for i in range(len(S)):
        if S[i]=='A' or S[i]=='E' or S[i]=='I' or S[i]=='O' or S[i]=='U':
            k+=len(S)-i
        else:
            s+=len(S)-i
    if s==k:
        print("Draw")
    elif k>s:
        print("Kevin "+ str(k))
    else:
        print("Stuart "+ str(s))

if __name__ == '__main__':
    s = input()
    minion_game(s)