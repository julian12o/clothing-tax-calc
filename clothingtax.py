#Julian Ortega, Smimeca, Ch. 2 Project: Your own Input, Processing, Output Program, 10/31 
price = float(input("Enter the price of the clothing item: "))
brand = input("Enter brand: ")
residence = input("Enter the location or delivery city: ")
amount = int(input("Enter how many you bought: "))
discount = float(input("Enter any discounts eg: 10 for 10%, 20 for 20%:"))

#calculations
subtotal = price * amount 
discount_amount = subtotal * (discount/ 100)
subtotal_after_discount = subtotal - discount_amount
tax_rate = 0.06625 #new jersey tax
total = subtotal_after_discount * (1 + tax_rate)
#summary
print("Purchase Summary")
print(f"Brand: {brand}")
print(f"Location: {residence}")
print(f"Quantity: {amount}")
print(f"Discount: {discount}")
print(f"Subtotal before discount: ${subtotal:.2f}")
print(f"Subtotal after discount: ${subtotal_after_discount:.2f}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Total with tax: ${total:.2f}")
print(f"You spent ${total:.2f} including tax.")
