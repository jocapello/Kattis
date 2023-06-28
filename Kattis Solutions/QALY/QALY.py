A = int(input())
D = 0
for i in range(A):
    B,C = map(float,input().split())
    D = D + B*C
print(D)
