num1 = list(map(int, input().split())) 
num2 = list(map(int, input().split())) 
num3 = list(map(int, input().split())) 
num4 = list(map(int, input().split())) 
num5 = list(map(int, input().split())) 

list = sum(num1) , sum(num2) , sum(num3) , sum(num4) , sum(num5)
X = max(list)
print(list.index(max(list))+1,X)

