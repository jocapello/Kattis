n = int(input())
for i in range(n):
    A, B, C = input().split()
    A = int(A)
    B = int(B)
    C = int(C)
    if (A+B)==C:
        print("Possible")
    elif (A-B)==C or (B-A)==C:
        print("Possible")
    elif (A*B)==C:
        print("Possible")
    elif (A/B)==C or (B/A)==C:
        print("Possible")
    else:
        print("Impossible")
    
