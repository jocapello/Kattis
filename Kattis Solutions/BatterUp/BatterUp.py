n = int(input())
list1 = []
list1 = str(input())

def Convert(string): 
    li = list(string.split(" ")) 
    return li 
list2=Convert(list1)
Sum=0
num=0
for i in range(n):
    if int(list2[i]) >= 0:
        num = num + 1
        Sum=Sum+int(list2[i])
print(Sum/num)
