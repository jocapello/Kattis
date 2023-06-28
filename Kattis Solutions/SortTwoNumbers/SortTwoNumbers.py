'''
Date : 01-07-2022
Solution to SortTwoNumbers 
By Jordan Capello

Written in Python
'''
n = list(map(int,input().split())) 
if n[0]<n[1]:
    print(n[0], n[1])
else:
    print(n[1], n[0])