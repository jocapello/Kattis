a,b = map(int,input().split())
c = 0

if a ==0 and b == 0:
    print("Not a moose")

if a == b and a != 0:
    c = a*2
    print("Even",c)
else:
    if a > b:
        c = a*2
        print("Odd",c)
    if a < b:
        c = b*2
        print("Odd",c)

