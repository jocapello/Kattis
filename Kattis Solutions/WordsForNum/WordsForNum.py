n=input()

TensList2=[20,30,40,50,60,70,80,90]
TensList=["twenty","thirty","forty","fifty","sixty","seventy","eighty","Ninety"]
ThruTenList2=[10,11,12,13,14,15,16,17,18,19]
ThruTenList=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
OnesList2=[1,2,3,4,5,6,7,8,9]
OnesList=["one","two","three","four","five","six","seven","eight","nine"]

Mylist=[]
# finds numbers in string
x=[int(s) for s in n.split() if s.isdigit()]
for i in range(len(x)):
    if x[i]>19:
        Tens=x[i]/10
        Ones=x[i]%10
        Tens=int(Tens)*10

        for i in range(len(TensList)):
                if TensList2[i]==Tens:
                    Number=TensList[i]
        
        for i in range(len(OnesList)):
                if OnesList2[i]==Ones:
                    Number=Number+str("-")+OnesList[i]
        Mylist.append(Number)
    else:
        for j in range(len(ThruTenList)):
            if x[i]==ThruTenList[j]:
                Mylist.append(ThruTenList[j])
Reword=n.split(" ")
for i in range(len(Reword)):
    for j in range(len(x)):
        if str(x[j])==str(Reword[i]):
            Reword[i]=Mylist[j]
print(' '.join(Reword))

