import math

Hours, Minutes = map(int,input().split())

if Hours < 1 and Minutes < 45:
    A=Minutes-45
    HM=(Hours*60)+Minutes
    Time=(HM-45)
    NUM = math.modf(Time/60)
    Minutes=NUM[0]*60

    print("23",int(((60-A)/100)*60))
if Hours == 0 and Minutes == 45:
    print(24, "00")
if Hours > 0:
    HM=(Hours*60)+Minutes
    Time=(HM-45)
    NUM = math.modf(Time/60)
    Minutes=NUM[0]*60
    print(int(NUM[1]),round(Minutes))
    # work on 0 to morning