for i in range(65,71):
    for j in range(65,71):
        print(chr(j),end=" ")
    print()
print("==================")
for i in range(65,71):               #if u want the same value repeating then we used use the outer loop 
    for j in range(65,71):           # if u want the value after one by one then we used the inner loop
        print(chr(i),end=" ")
    print()

    