NumTasks,Min= map(int,input().split())
Tasks = list(map(int,input().split()))
Count=0
total=0
for i in range(NumTasks):
    Count+=Tasks[i]
    if Count<=Min:
        total+=1
    if Count>=Min:
        break
print(total)

