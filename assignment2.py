# PART ONE

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
    min_down_payment = (0.05 * 500000) + (0.1 * (purchase_price - 500000))
elif purchase_price > 1000000:
    min_down_payment = purchase_price * 0.2
min_down_payment = int(min_down_payment)
print(f"The minimum down payment allowed is ${min_down_payment}")

# Determine Percent
down_dec = (min_down_payment / purchase_price)
down_perc = (min_down_payment / purchase_price) * 100
down_payment = purchase_price * down_perc / 100
print(down_payment)

# Input Percent
chosen_perc = input("Enter desired percantage for down payment: %")
chosen_perc = int(chosen_perc)
down_payment = purchase_price * chosen_perc / 100

# Insurance Cost
if chosen_perc >= 5 and chosen_perc < 10:
    insurance_cost = (purchase_price - down_payment) * (4 / 100)
elif chosen_perc >= 10 and chosen_perc < 15:
    insurance_cost = (purchase_price - down_payment) * (3.1 / 100)
elif chosen_perc >= 15 and chosen_perc < 20:
    insurance_cost = (purchase_price - down_payment) * (2.8 / 100)
elif chosen_perc >= 20:
    insurance_cost = 0
print(insurance_cost)

# Principal Amount
princ_amount = purchase_price - down_payment + insurance_cost
print(f"The principal amount is ${princ_amount}")

