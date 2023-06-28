D1,D2 = map(int,input().split())
X,Y = map(int,input().split())
n = int(input())

# n-1 
Max = 0
if D1 < D2:
    Max = D1
else:
    Max = D2

ans = 0
Out = []

for i in range(n):
    if X==Y:
        ans+=1
    
    w = input().split(" ")
    if w[1].startswith("u"):
        Y=Y+int(w[0])
    if w[1].startswith("r"):
        X=X+int(w[0])
    if w[1].startswith("d"):
        Y=Y-int(w[0])
    if w[1].startswith("l"):
        X=X-int(w[0])
    temp = X,Y
    if ans+1<=Max:
        Out.append(temp)
if len(Out)==n:
    for i in range(n):
        print((Out[i]))
if len(Out)<n:
    for i in range(len(Out)-1):
        print((Out[i]))