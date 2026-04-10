pin = int(input("press the pin: "))

if 1000 <= pin <= 9999:
    print("Valid 4-digit PIN")
else:
    print("Invalid PIN")