import math
A,B,C = map(int,input().split())
Hyp = math.sqrt((B*B)+(C*C))
print(Hyp)
for i in range(A):
    D = int(input())
    if D <= Hyp:
        print("DA")
    else:
        print("NE")