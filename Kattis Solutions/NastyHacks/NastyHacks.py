import sys

def DoMath(n):
    r,e,c = map(int,input().split())
    if e-c > r:
        print ("advertise")
        #list1[i] = ("advertise")
    if e-c == r:
        print ("does not matter")
        #list1[i] = ("does not matter")
    if e-c < r:
        print ("do not advertise")
        #list1[i] = ("do not advertise")

n = input()
list1 = ['','','','','','','','','','']
for i in range(int (n)):
    DoMath(n)
#for i in range(int (n)):
  #  print(list1[i])