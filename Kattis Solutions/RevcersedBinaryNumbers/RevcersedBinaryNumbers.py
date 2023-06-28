'''
Date : 01-08-2022
Solution to Reversed Binary Numbers
By Jordan Capello

Written in Python
'''
n = int(input())
n = bin(n)[2:]
print(int((n[::-1]),2))


