from collections import Counter
n=int(input())

for i in range(n):
    x=int(input())
    Guests = list(map(int, input().split()))
    Pom=Counter(Guests)
    for j in range(len(Guests)):
        for k in range(len(Guests)):
            if Guests[j] == Guests[k] and j != k:
                Guests[j]=''
                Guests[k]=''
    for l in range(len(Guests)):
        if Guests[l]!='':
            print('Case #',i+1,': ',Guests[l],sep='')
