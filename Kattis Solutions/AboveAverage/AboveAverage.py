n = int(input())

def check(list1, val): 
    for x in list1: 
        if val>= x: 
            return False 
    return True

for i in range(n):
    list1=list(map(int,input().split()))
    Sum=sum(list1)-list1[0]
    num1=int(list1[0])
    Mean=Sum/num1
    Above = 0
    for i in list1:
        if i>int(Mean):
            Above+=1
    x=(Above/num1)*100
    print("%0.3f"%x,end="")
    print('%')
    Sum=0
    num1=0
    Mean=0
# Above doesnt work for unknown reason, bottom one does
#     C = int(input())

# for _ in range(C):
#     N, *grades = tuple(map(int, input().split()))

#     mean = sum(grades) / N

#     above = 0
#     for grade in grades:
#         if grade > mean:
#             above += 1
    
#     print("%.3f%s" % (round(above / N * 100, 3), '%'))
