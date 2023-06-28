T=int(input())

for i in range(T):
    Ans=1
    n=int(input())
    for i in range(1,n+1):
        Ans=Ans*i
    print(Ans%10)