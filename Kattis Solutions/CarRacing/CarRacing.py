import math
n = int(input())
x = []
for i in range(n):
    x.append(input().split(" "))


Car1 = []
Car2 = []
Car3 = []
Car4 = []
Car5 = []

for i in range(n):
    if x[i][0]=="1":
        Car1.append(int(x[i][1]))
    if x[i][0]=="2":
        Car2.append(int(x[i][1]))

    if x[i][0]=="3":
        Car3.append(int(x[i][1]))

    if x[i][0]=="4":
        Car4.append(int(x[i][1]))

    if x[i][0]=="5":
        Car5.append(int(x[i][1]))



Ans = sum(Car1)/len(Car1), sum(Car2)/len(Car2), sum(Car3)/len(Car3), sum(Car4)/len(Car4), sum(Car5)/len(Car5)


if (Ans[0]) == min(Ans):
    print(1)
    print(math.floor(Ans[0]))
if (Ans[1]) == min(Ans):
    print(2)
    print(math.floor(Ans[1]))
if (Ans[2]) == min(Ans):
    print(3)
    print(math.floor(Ans[2]))
if (Ans[3]) == min(Ans):
    print(4)
    print(math.floor(Ans[3]))
if (Ans[4]) == min(Ans):
    print(5)
    print(math.floor(Ans[4]))