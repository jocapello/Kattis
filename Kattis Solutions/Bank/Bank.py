
CustomerNum,MinClose= map(int,input().split())
Money=[]
Time=[]
for i in range(CustomerNum):
    C,D = map(int,input().split())
    if D<=MinClose:
        Money.append(-C)
        Time.append(D)

# SORT A LIST BASED ON ANOTHER LIST
#===================================
zipped_lists = zip(Money, Time)
sorted_pairs = sorted(zipped_lists)

tuples = zip(*sorted_pairs)
Money, Time = [ list(tuple) for tuple in  tuples]

print(Money)
print(Time)
Largest=[]

for i in range(CustomerNum):
    Largest.append(Money[i])
#print(sorted_list1)
#===================================


# for i in range(len(Time)-1):
#     if Time[i] == Time[i+1]:
#         if Money[i]>=Money[i+1]:
#             del Time[i+1]
#             del Money[i+1]
#             i=0
#         else:
#             del Time[i]
#             del Money[i]


# print(sum(Money))
