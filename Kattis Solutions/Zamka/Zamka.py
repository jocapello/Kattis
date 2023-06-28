A=int(input())
B=int(input())
C=int(input())
D=0
list = []
for i in range(A,B+1):
    if sum(map(int, str(i)))==C:
        list.append(i)
print(min(list))
print(max(list))