Int=input()
MyString=[]
for i in Int:
    if i == "<" and len(MyString)>0:
        MyString.pop()
    else:
        MyString.append(i)
print(''.join(MyString))