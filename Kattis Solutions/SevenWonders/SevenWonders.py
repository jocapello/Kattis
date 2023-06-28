from collections import Counter

n=list(input())
counter=Counter(n)
Tab=counter['T']
Com=counter['C']
Gear=counter['G']

SetList=Tab,Com,Gear
Score=Tab**2+Com**2+Gear**2
Min=min(SetList)
if Min > 0:
    Score=Score+(7*Min)
print(Score)