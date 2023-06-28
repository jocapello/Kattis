
Letter = ["w","r","g","b","y","a","f","s","m","o","i","e","u","h","p","c"]
Colours = [(255,255,255),(255,0,0),(0,255,0),(0,0,255),(255,255,0),(255,0,255),(192,192,192),(128,0,0),(255,165,0),
        (75,0,130),(80,200,120),(18,10,143),(165,42,42),(255,192,203),(220,20,60)]
n = int(input())
word = []
dif = []
ColourX = []
ColourY = []
ColourZ = []

for i in range(n):
    ColourX = input().split(" ")
    ColourX.append(int(ColourX[0]))
    ColourY.append( int(ColourX[1]))
    ColourZ.append(int (ColourX[2]))

print(ColourX)
# for i in range(len(Letter)):
#     X = sum(Colours[i])-int(sum(ColourX))
#     dif.append(X)
print((dif))    
