n=int(input())
Num=[]
for i in range(n):
    Num.append(int(input()))
Num.sort()
print(Num)
Ans=[]
for i in range(len(Num)):
    if Num[i] != Num[i+1]+1:
        Ans.append(Num[i]+1)
print(Ans)