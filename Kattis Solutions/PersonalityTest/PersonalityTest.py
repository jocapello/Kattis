import Numpy as np
  
  
# create array
x = np.array([1,2,3,4,5,1,2,1,1,1])
print("Original array:")
print(x)
  
print("Most frequent value in the above array:")
print(np.bincount(x).argmax())


n = int(input())
x = []

for i in range(n):
    x.append(input())



for i in range(n):
    print(np.bincount(x).argmax())
