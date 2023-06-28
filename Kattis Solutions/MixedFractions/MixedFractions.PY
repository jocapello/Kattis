import math
while True:
  n1, n2 = input().split()
  n1 = int(n1)
  n2 = int(n2)
  if n1 == 0 and n2 == 0:
    break;
  else:
    temp = n1/n2
    # Seperates whole num from fractions, frac and whole are the variables it goes into
    frac, whole = math.modf(temp)
    print(round(whole), round(frac*n2), "/", n2)