Y=0
X=0
Reverse=0
def NEW(X):
    global Reverse
    while(X > 0):    
        Reminder = X %10    
        Reverse = (Reverse *10) + Reminder  
        X = X //10
    return Reverse
A,B = map(int,input().split())
C = NEW(A)
X=0
Reminder=0
Reverse=0
D = NEW(B)
if C > D:
    print(C)   
else:
    print(D)
