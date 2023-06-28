A = int(input())
E = 0
for i in range(A):
    B = int(input())
    # last digit
    C = B % 10
    # all but last digit
    D = int(B/10)
    E = pow(D,C) + E
print(E)