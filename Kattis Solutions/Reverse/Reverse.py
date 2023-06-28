'''
Date : 01-08-2022
Solution to Reverse
By Jordan Capello

Written in Python
'''
n = int(input())
p = []
for i in range(n):
    p.append(input())
print('\n'.join(map(str,p[::-1])))