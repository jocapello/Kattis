n = int(input())
list = list(map(int, input().split()))
X = min(list)
for i in range(len(list)):
    if X == list[i]:
        print(i)
        exit()
