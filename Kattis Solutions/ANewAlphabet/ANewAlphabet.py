MyString=str(input())
Alphabet={  "A": "@","B": "8","C": "(","D": "|)","E": "3","F": "#","G": "6","H": "[-]","I": "|",
    "J": "_|","K": "|<","L": "1","M": "[]\\/[]","N": "[]\\[]","O": "0","P": "|D","Q": "(,)",
    "R": "|Z","S": "$","T": "']['","U": "|_|","V": "\\/","W": "\\/\\/","X": "}{","Y": "`/","Z": "2"}

MyString = MyString.upper()
NewWord=[]
for i in range(len(MyString)):
    if Alphabet.get(MyString[i])!=None:
        NewWord.append(Alphabet.get(MyString[i]))
    if Alphabet.get(MyString[i])==None:
        NewWord.append(MyString[i])
    
print(''.join(NewWord))