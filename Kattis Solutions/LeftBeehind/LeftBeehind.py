while True:
    A,B = map(int,input().split())
    if A + B == 0:
        exit()
    elif A + B == 13:
        print("Never speak again.")
    elif A > B:
        print("To the convention.")
    elif A < B:
        print("Left beehind.")
    elif A == B and A != 0:
        print("Undecided.")
