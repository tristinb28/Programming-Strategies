# Inputs :)
client_name = input("Enter Clients Name: ")
address = input("Enter House Address: ")
purchase_price = input("Enter Purchase Price of Property (No Commas or Decimals): $")
if purchase_price.isdigit():
    purchase_price = int(purchase_price)
else:
    print("Error: Please enter a valid integer for the purchase price.")

# Calculate minimum down payment
if purchase_price <= 500000:
    min_down_payment = purchase_price * 0.05
elif purchase_price > 500000 and purchase_price <= 1000000:
    min_down_payment = (0.05 * 500000) + (0.10 * (purchase_price - 500000))
elif purchase_price > 1000000:
    min_down_payment = purchase_price * 0.2
min_down_payment = int(min_down_payment)
print(f"The minimum down payment allowed is ${min_down_payment}")

down_dec = (min_down_payment / purchase_price)
down_perc = (min_down_payment / purchase_price) * 100
print(f"The Minimum down payment percent is %{down_perc}")
down_payment = purchase_price * down_dec
print(down_payment)
print(f"%{down_perc}")

if down_perc >= 5 and down_perc < 10:
    insurance_rate = (purchase_price - min_down_payment) * (4 / 100)
    print("first if statement calculated")
elif down_perc >= 10 and down_perc < 15:
    insurance_rate = (purchase_price - min_down_payment) * (3.1 / 100)
    print("second if statement calculated")
elif down_perc >= 15 and down_perc < 20:
    insurance_rate = (purchase_price - min_down_payment) * (2.8 / 100)
    print("third if statement calculated")
elif down_perc >= 20:
    insurance_rate = 0
    print("fourth if statement calculated")
print(insurance_rate)