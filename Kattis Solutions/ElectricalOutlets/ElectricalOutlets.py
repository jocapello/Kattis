'''
Date : 01-08-2022
Solution to Electrical Outlets
By Jordan Capello

Written in Python
'''
n = int(input())
for i in range(n):
    r = list(map(int,input().split())) 
    t = r[0]
    r.remove(r[0])
    print(sum(r)-(t-1))
    
