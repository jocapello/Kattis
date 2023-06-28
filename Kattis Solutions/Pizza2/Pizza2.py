import math
R,C= map(int,input().split())
Area=R**2 #Total area
Che=float(R-C)**2 #Area of cheese
Per=(Che/Area)*100
print("{:.6f}".format(Per));
