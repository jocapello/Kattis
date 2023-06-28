n = input()
List1=[]
def Char(Char):
    for i in range(len(n)):
        if str(Char) in n:
            List1.append("{")
            X=n.split("{")
    print(X)

print(Char(n))