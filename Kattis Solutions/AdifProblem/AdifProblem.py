import sys
for line in sys.stdin.readlines(): # for every line inputted from the file 
   a,b = map(int,line.split())
   print(abs(a-b))