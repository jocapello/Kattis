n=0
Hours=0
OldHours=0
Distance=0
while n != -1:
    n=int(input())
    if n != -1:
        for i in range(n):
            Speed,Hours = map(int,input().split())
            Distance=Distance+(Speed*(Hours-OldHours))
            OldHours=Hours
        print(Distance,"miles")
        Distance=0
        Speed=0
        OldHours=0
