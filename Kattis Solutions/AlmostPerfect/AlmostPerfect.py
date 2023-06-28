'''
Date : 01-08-2022
Solution to Almost Perfect
By Jordan Capello

Written in Python
'''
import math

def factors(n):
    l = []
    for i in range(1,int(math.sqrt(n))+1):
        if n % i == 0:
            l.append(i)
            if int(n/i) != i:
                l.append(int(n/i))
    return l

while True:
    try:
        n = int(input())
        #print(factors(n), sum(factors(n)))
        ans = sum(factors(n))-n
        if ans == n:
            print(n, "perfect")
        elif ans == n + 2 or ans == n - 2 or ans == n + 1 or ans == n - 1:
            print(n, "almost perfect")
        else:
            print(n, 'not perfect')

    except EOFError:
        break





# import sys
# import math

# for line in sys.stdin.readlines(): # for every line inputted from the file 
#     Number=int(input())
#     Sum=1
#     Sqr=math.sqrt(Number)
#     for i in range(2, Number):
#         if i < Sqr:
#             if Number % i == 0:
#                 Sum=Sum+i
#                 Sum=Sum+Number/i
#     if Sqr * Sqr == Number:
#         Sum=Sum+Sqr
#     if Sum == Number:
#         print(Number, 'perfect')
#     elif Sum - 2 == Number or Sum - 1 == Number or Sum + 2 == Number or Sum + 1 == Number:
#         print(Number, 'almost perfect')
#     else:
#         print(Number, 'not perfect')

