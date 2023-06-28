A,B,C= map(int,input().split())

if A+B==C:
    A = str(A)
    B = str(B)
    C = str(C)
    X=A,"+",B,"=",C
elif A==B+C:
    A = str(A)
    B = str(B)
    C = str(C)
    X=A,"=",B,"+",C

elif A-B==C:
    A = str(A)
    B = str(B)
    C = str(C)
    X=A,"-",B,"=",C

elif A==B-C:
    A = str(A)
    B = str(B)
    C = str(C)
    X=A,"=",B,"-",C

elif A*B==C:
    A = str(A)
    B = str(B)
    C = str(C)
    X=A,"*",B,"=",C
elif A==B*C:
    A = str(A)
    B = str(B)
    C = str(C)
    X=A,"=",B,"*",C

elif A/B==C:
    A = str(A)
    B = str(B)
    C = str(C)
    X=A,"+",B,"=",C

elif A==B/C:
    A = str(A)
    B = str(B)
    C = str(C)
    X=A,"=",B,"/",C
print("".join(X))