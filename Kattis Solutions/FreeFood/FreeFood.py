n = input()
C=0
Mylist=[]
for i in range(int (n)):
    A,B= map(int,input().split())
    for i in range(B-A+1):
        C=A+i
        Mylist.append(C)
a_set = set(Mylist)
num = len(a_set)
print(num)