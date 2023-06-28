'''
Date : 01-07-2022
Solution to OddEcho 
By Jordan Capello

Written in Python
'''

n = int(input())

nm = []
for i in range(1,n+1):
    word = input()
    if i %2 != 0:
        nm.append(word)
print('\n'.join(map(str,nm)))
