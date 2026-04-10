num = int(input("Enter number: "))

last_digit = num % 10
square = last_digit ** 2

if square > 10:
    print("Condition satisfied")
else:
    print("Condition not satisfied")