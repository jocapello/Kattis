n = int(input())
for i in range(n):
    A,B,C = map(str,input().split())
    A = int(A)
    B = int(B)
    C = int(C)
    Answer=0
    while A<=C:
        A=A*B
        Answer=Answer+1
    print(Answer)
        
