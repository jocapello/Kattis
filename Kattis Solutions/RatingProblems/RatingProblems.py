'''
Date : 01-07-2022
Solution to Rating Problems 
By Jordan Capello

Written in Python
'''
rating = 0
n = list(map(int,input().split())) 
for i in range(n[1]):
    rating = rating + (int(input()))
min = (rating + (n[0]-n[1])*-3)/n[0]
max = (rating + (n[0]-n[1])*3)/n[0]

print(min,max)