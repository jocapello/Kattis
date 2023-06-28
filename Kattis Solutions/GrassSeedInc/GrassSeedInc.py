n=float(input())
w=int(input())
C=0
for i in range(w):
    A,B=map(float,input().split())
    C=C+(A*B)
C=C*n
print("%0.6f"%C)