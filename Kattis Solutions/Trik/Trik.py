import collections
def split(word): 
    return [char for char in word]  

A = input()
B = split(A)
num = ["Ball","Y","Z"]
for i in range(len(B)):
    if B[i]=="A":
        temp=num[0]
        num[0]=num[1]
        num[1]=temp
    if B[i]=="B":
        temp=num[1]
        num[1]=num[2]
        num[2]=temp
    if B[i]=="C":
        temp=num[2]
        num[2]=num[0]
        num[0]=temp
if num[0]=="Ball":
    print("1")
if num[1]=="Ball":
    print("2")
if num[2]=="Ball":
    print("3")

