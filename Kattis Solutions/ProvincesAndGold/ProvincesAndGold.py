'''
Date : 01-08-2022
Solution to Anagram Counting
By Jordan Capello

Written in Python
'''
g,s,c = map(int,input().split())
My_dict = {"Provice":8, "Duchy":5, "Estate":2, "Gold":6, "Silver":3, "Copper":0}
value = 3*g+2*s+c
if value >= 8:
    print("Province or Gold")
elif value >= 6:
    print("Duchy or Gold")
elif value >= 5:
    print("Duchy or Silver")
elif value >= 3:
    print("Estate or Silver")
elif value >= 2:
    print("Estate or Copper")
else:
    print("Copper")