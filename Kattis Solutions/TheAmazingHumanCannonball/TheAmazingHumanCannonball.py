'''
Date : 01-08-2022
Solution to The Amazing Human Cannonball
By Jordan Capello

Written in Python
'''
import math

n = int(input())
for i in range(n):
    a,b,c,d,e = map(float,input().split())
    t = c/(a*(math.cos(math.radians(b))))
    y = (a*t*math.sin(math.radians(b))) - ((4.905)*(t**2))
    if (y-1 >= d and y+1 <= e):
        print('Safe')
    else:
        print('Not Safe')  
