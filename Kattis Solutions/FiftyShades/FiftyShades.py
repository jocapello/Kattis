n=int(input())
Ans=0
for i in range(n):
    word=input()
    word=word.lower()
    if 'rose' in word or 'pink' in word:
        Ans=Ans+1
if Ans > 0:
    print(Ans)
else:
    print('I must watch Star Wars with my daughter')