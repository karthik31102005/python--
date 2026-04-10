num = int(input("Enter number: "))

if num % 4 == 0 and num % 6 != 0:
    print("Divisible by both 4 and but not 6")
else:
    print("Not divisible by both")