list = map(int,input().split())
list=sorted(list)

def split(word): 
    return [char for char in word]

A=list[0]
B=list[1]
C=list[2]
s=input()
y = split(s)

for i in range(len(y)):
    if y[i]=='A':
        print(A,end=' ')
    if y[i]=='B':
        print(B,end=' ')
    if y[i]=='C':
        print(C,end=' ')
