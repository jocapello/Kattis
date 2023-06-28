A,B,C = map(int,input().split())
for i in range(1,C+1):
    if i % A == 0 and i % B == 0:
        print("FizzBuzz")
    elif i % A == 0:
        print("Fizz")
    elif i % B == 0:
        print("Buzz")
    else:
        print(i)
    
