run = True
while run:
    ans=0
    a, b = map(int, input().split())
    if a + b == 0:
        exit()
    list = []
    for i in range(a):
        r = input()
        if r == "0 0":
            print(ans)
            exit()
        list.append(r)
    for i in range(b):
        x = input()
        if x == "0 0":
            print(ans)
            exit()
        if x in list:
            ans = ans + 1
    print(ans)
    c,d = map(int, input().split())
    run = False


# import sys

# def main():
#     while True:
#         n,m = [int(i) for i in sys.stdin.readline().split()]
#         set1 = set()
#         if n==0 and m==0:
#             break
#         for i in range(n):
#             set1.add(int(sys.stdin.readline().strip()))

#         count = 0
#         for j in range(m):
#             count += int(sys.stdin.readline().strip()) in set1
#         print (count)

# if __name__ == '__main__':
#     main()