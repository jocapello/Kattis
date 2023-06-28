RowOne = list(map(int,input().split()))
RowTwo = list(map(int,input().split()))
RowThree = list(map(int,input().split()))
RowFour = list(map(int,input().split()))
Move = int(input())

def Math(Row):

    if Move == 0:
        for i in range(len(Row)):
            if i<=2:
                if Row[i]==Row[i+1]:
                    Row[i+1]=Row[i]*2
                    Math(Row)
            if i==0:
                if Row[i+1]==0 and Row[i+2]==0 and Row[i+3]==0:
                    Row[i+3]=Row[i]
                    Row[i]=0
            if i<=1:
                if Row[i+1]==0 and Row[i+2]==0:
                    Row[i+2]=Row[i]
                    Row[i]=0
            if i<=2:
                if Row[i+1]==0 :
                    Row[i+1]=Row[i]
                    Row[i]=0

for i in range(len(list(RowOne))):
    if i == 0:
        Math(RowOne)
        print(RowOne)
    if i == 1:
        Math(RowTwo)
        print(RowTwo)
    if i == 2:
        Math(RowThree)
        print(RowThree)
    if i == 3:
        Math(RowFour)
        print(RowFour)
