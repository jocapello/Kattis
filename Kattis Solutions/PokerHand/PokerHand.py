a,b,c,d,e = map(str,input().split())

def split(word): 
    return [char for char in word]  

split(a)
f=split(a)
split(b)
g=split(b)
split(c)
h=split(c)
split(d)
i=split(d)
split(e)
j=split(e)

A='A'
B='2'
C='3'
D='4'
E='5'
F='6'
G='7'
H='8'
I='9'
J='T'
K='J'
L='Q'
M='K'


list = [f[0],g[0],h[0],i[0],j[0]]
count = list.count(A)
count1 = list.count(B)
count2 = list.count(C)
count3 = list.count(D)
count4 = list.count(E)
count5 = list.count(F)
count6 = list.count(G)
count7 = list.count(H)
count8 = list.count(I)
count9 = list.count(J)
count10 = list.count(K)
count11 = list.count(L)
count12 = list.count(M)
list1=[count,count1,count2,count3,count4,count5,count6,count7,count8,count9,count10,count11,count12]
print(max(list1))