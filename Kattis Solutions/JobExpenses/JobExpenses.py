n = input()
list = list(map(int,input().split()))
Sum=0
for i in range(len(list)):
    if list[i]<0:
        Sum=Sum+list[i]
print(-Sum)

