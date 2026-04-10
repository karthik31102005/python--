str='PAVANKARTHIK'
print(str[-2])
print(str[::-1])
for i in str:
    print(i,end=" ")
print("backward direction")
for i in str[-1::-2]:
    print(i,end=" ")
print("/n")
i=0
while i<len(str):
    print(str[i],end=" ")
    i+=1