n=list(input())

score=[0,0]

for i in range(len(n)-1):
    if n[i]=='A':
        score[0]=score[0]+int(n[i+1])
    if n[i]=='B':
        score[1]=score[1]+int(n[i+1])
if score[0]>score[1]:
    print('A')
else:
    print('B')
    