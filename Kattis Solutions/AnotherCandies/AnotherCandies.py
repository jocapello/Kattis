Sets=int(input())

for i in range(Sets):
    x=input()
    Candy=0
    Students=int(input())

    for i in range(0,Students):
        
        Candy=Candy+int(input())

    if Candy % Students ==0:
        print("YES")
    else:
        print("NO")
