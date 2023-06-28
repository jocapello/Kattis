A,B,C= map(int,input().split())
MyCords=A,B
MyList=[]
MyList2=[]
def Cords(MyList2):
    for i in range(3):
        #far right
        MyList3=int(MyList2[0])+int(MyList2[2]),MyList2[1]
        #top
        MyList4=MyList2[0],int(MyList2[1])-int(MyList2[2])
        #bottom
        MyList5=MyList2[0],int(MyList2[1])+int(MyList2[2])
        #left
        MyList6=int(MyList2[0])-int(MyList2[2]),int(MyList2[1])

    return MyList3,MyList4,MyList5,MyList6

    print(MyList2," r")
result=[]
for i in range(C):
    MyList.append(input())
    MyList2.append(MyList[i].split(" "))
    result=Cords(MyList2[i])
    print(result)
