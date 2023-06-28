A=input()
n=input()
numbers = []
numbers2 = []
WORD=[]
n=n.lower()
A=A.lower()
Alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","Q","R","S","T","U","V","W","X","Y","Z"]
for letter in (n):
  number = ord(letter) - 97
  numbers.append(number)
for letter in (A):
  number2 = ord(letter) - 97
  numbers2.append(number2)
for i in range(len(numbers)):
  numbers2[i]=numbers2[i]+numbers[i]
  if (numbers2[i]>25):
    numbers2[i]=numbers2[i]-26
print(numbers2)
for i in range(len(numbers2)):
  WORD.append(Alphabet[numbers2[i]])
print(WORD)
