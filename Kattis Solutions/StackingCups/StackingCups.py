n = int(input())
list = []
list2 = []

def IntFirst(X):
    try:
        i = int(X)
    except:
        return False
    return True
  

for i in range(n):
    line = input().split()

    if IntFirst(line[0]) == True:
        list2.append((int(line[0])/2, line[1]))
    else:
        list2.append((int(line[1]),line[0]))
list2= sorted(list2)

for pair in list2:
    print(pair[1])


    
