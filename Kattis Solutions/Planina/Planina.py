'''
Date : 01-07-2022
Solution to Planina
By Jordan Capello

Written in Python
'''
def calculate(n,ans):
    if n <= 0:
        r = (ans+2)**2
        print(r)
    else:
        calculate(n-1,ans + 2**(n-1))

n = int(input())
calculate(n,0)
