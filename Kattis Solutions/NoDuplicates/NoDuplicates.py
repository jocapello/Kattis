list = []

def unique(list1): 

    # intilize a null list 
    unique_list = [] 

    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x)
    y = len(unique_list)
    if y < len(list1):
        print("no")
    else:
        print("yes")

a, *list = input().split()
list.append(a)
unique(list)