'''n = 321875

while n > 0:
    digit = n % 10
    
    if digit % 2 == 0:
        print(digit, "is even")
    
    n = n // 10'''
n = 321875

last_digit = n % 10

if last_digit % 2 == 0:
    print("Last digit is even")
else:
    print("Last digit is odd")