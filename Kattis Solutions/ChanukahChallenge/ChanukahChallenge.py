n = input()
Number=[]
C=0
for i in range(int (n)):
    A,B= map(int,input().split())
    C=int(B)*((int(B+1))/2)+B
    print(int(A),round(C))




    # line = input().split() // easier line splitter
    # print(F"{line[0]} {int(int(line[1]) * (int(line[1])+1) / 2 + int(line[1]))}") // Way of printing arrays without brackets 