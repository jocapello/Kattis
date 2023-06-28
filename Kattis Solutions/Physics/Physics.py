import random

Names = ["Courtney","Seth","Vince","Jordan",
    "Mia","Jin","Amber","Titus",
    "Sophia","Kelsey","Ryan","Ella"]

Group = [["0","0","0","0"],
         ["0","0","0","0"],
         ["0","0","0","0"]]
i=0
def Checker():
    for i in range(len(Names)):
        r=random.randint(0,11)
        if Names[r]=="0":
            Checker(Names)
        if Names[r]!="0":
            if r<4 and i<4:
                print(Names[r])
                x = Group[0]
                x.append(Names[r])
                i=i+1
Checker()
print(Group)



    


