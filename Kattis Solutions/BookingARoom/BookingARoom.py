import random

list = []
list2 = []
list3 = []
A,B, = map(int,input().split())


for i in range(B):
    list.append(int(input()))
if A == B:
    print("too late")
    exit()
for i in range(1,A+1):
    list2.append(i)
list3 = [x for x in list2 if x not in list]

X=random.randint(1,A-B)
print(list3[X-1])

    


    



