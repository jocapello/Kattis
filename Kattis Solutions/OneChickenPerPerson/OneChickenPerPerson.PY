A,B = map(int,input().split())

C = 0 

C = B - A
if C == -1:
    print("Dr. Chaz needs 1 more piece of chicken!")
if C < -1:
    print("Dr. Chaz needs",(-C),"more pieces of chicken!")
if C == 1:
    print("Dr. Chaz will have 1 piece of chicken left over!")
if C > 1:
    print("Dr. Chaz will have",(C),"pieces of chicken left over!")

