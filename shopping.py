pid=int(input("Enter product ID: "))
pname=input("Enter product name: ")
price=float(input("Enter product price: "))
quantity=int(input("Enter product quantity: "))
print(f"Product ID: {pid}, Product Name: {pname}, Price: {price}, Quantity: {quantity}")
total_cost = price * quantity
print("======== calculate discount ========")
discount = 0.0
if total_cost > 2000:
    discount = (total_cost * 10) / 100
elif total_cost > 2000 and total_cost <= 5000:
    discount = (total_cost * 15) / 100
elif total_cost > 5000:
    discount = (total_cost * 31) / 100
gst = (total_cost * 18) / 100
invoice_bil=(total_cost - discount) + gst
print(f"Total cost: {total_cost}")
print(f"Discount: {discount}")  
print(f"GST: {gst}")
print(f"Invoice Bill: {invoice_bil}")