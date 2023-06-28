import math
A,B = map(int,input().split())
E = 0
Denied = 0
for i in range(B):
    C,D = map(str,input().split())
    if C == "enter":
        if E + int(D) <= A:
            E = E + int(D)
        else:
            Denied=Denied+1
    if C == "leave":
        E = E - int(D)
print(Denied)
   