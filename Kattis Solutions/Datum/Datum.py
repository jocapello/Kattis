
import datetime 
import calendar 
  
def findDay(date): 
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday() 
    return (calendar.day_name[born]) 

A,B= map(int,input().split())
if A < 10:
    A=str(A)
    A="0",A
    A=''.join(A)
else:
    A=str(A)
if B < 10:
    B=str(B)
    B="0",B
    B=''.join(B)
else:
    B=str(B)
# change the date from 2009 to anything
C=A,B,'2009'
C=" ".join(C)
# Driver program 

print(findDay(C)) 