bill = float(input("Enter total bill amount: "))
member = input("Are you a member (yes/no): ")

if member.lower() == "yes" and bill > 1000:
    discount = bill * 0.10
else:
    discount = 0

final_amount = bill - discount

print("Discount:", discount)
print("Final Bill:", final_amount)