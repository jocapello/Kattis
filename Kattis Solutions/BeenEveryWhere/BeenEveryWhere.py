from collections import Counter
Useless = int(input())

for i in range(Useless):
    Mylist=[]
    answer=0
    x = int(input())
    for i in range(x):
        w = input()
        Mylist.append(w)
    Ans=len(list(Counter(Mylist).keys()))
    print(Ans)

