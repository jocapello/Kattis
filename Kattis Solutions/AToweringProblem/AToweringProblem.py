from collections import OrderedDict

Boxes=list(map(int,input().split()))

Height1=int(Boxes[6])
Height2=int(Boxes[7])
Boxes=sorted(Boxes)
print(Boxes)
Mylist=[]
Mylist2=[]
for i in range(6):
    for j in range(6):
        for k in range(6):
            if Boxes[i]+Boxes[j]+Boxes[k]==Height1:
                x=Boxes[i],Boxes[j],Boxes[k]
                Mylist.append(x)
for i in range(6):
    for j in range(6):
        for k in range(6):
            if Boxes[i]+Boxes[j]+Boxes[k]==Height2:
                x=Boxes[i],Boxes[j],Boxes[k]
                Mylist2.append(x)
for i in range(len(Mylist)):
    Mylist[i]=sorted((Mylist[i]))
Mylist=sorted(Mylist, reverse = True)
for i in range(len(Mylist)-1):
    if Mylist[i]==Mylist[i+1]:
        Mylist[i]=Mylist[i].pop()
#Mylist=sorted(Mylist, reverse = True)

            
for i in range(len(Mylist2)):
    Mylist2[i]=sorted((Mylist2[i]))
Mylist2=sorted(Mylist2, reverse = True)
for i in range(len(Mylist2)-1):
    if Mylist2[i]==Mylist2[i+1]:
        print(Mylist2[i])  
        Mylist2[i]=0 
        print(Mylist2[2])   
        Mylist2[i]=Mylist2[i].pop()
        print(Mylist2[i])
#Mylist2=sorted(Mylist2, reverse = True)


print(Mylist,'\n')
print(Mylist2)
print(Boxes)
