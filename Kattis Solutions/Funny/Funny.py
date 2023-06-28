print(7%5)

a = int(input())
b = int(input())
m = int(input())
n = 1
subjects = []
verbs = []
objects = []
places = []
Ans = []

for i in range(m):
    subjects.append(input())
for i in range(m):
    verbs.append(input())
for i in range(m):
    objects.append(input())
for i in range(m):
    places.append(input())

Ans = []
temp = []
for i in range(m):
    mod = int((a*n + b) % m)
    Ans.append(subjects[mod])
    n = mod
    mod = int((a*n + b) % m)
    Ans.append(verbs[mod])
    n = mod
    mod = int((a*n + b) % m)
    Ans.append(objects[mod])
    n = mod
    mod = int((a*n + b) % m)
    Ans.append(places[mod])

print()
i=0
print(Ans[i],Ans[i+1],Ans[i+2],Ans[i+3]+".")
i=12
print(Ans[i],Ans[i+1],Ans[i+2],Ans[i+3]+".")
i=4
print(Ans[i],Ans[i+1],Ans[i+2],Ans[i+3]+".")
i=16
print(Ans[i],Ans[i+1],Ans[i+2],Ans[i+3]+".")
i=8
print(Ans[i],Ans[i+1],Ans[i+2],Ans[i+3]+".")

i=20

