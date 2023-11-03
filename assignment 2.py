# PART ONE
# Inputs
client_name = input("Enter client name: ")
property_address = input("Enter address of property: ")

# Input Purchase Price and validate
purchase_price = input("Enter purchase price: $")
if purchase_price.isdigit():
    purchase_price = int(purchase_price)
else:
    print("Error: Please enter a valid integer for the purchase price.")
    exit()

# Calculate minimum down payment
if purchase_price <= 500000:
    min_down_payment = purchase_price * 0.05
elif 500000 < purchase_price <= 1000000:
    min_down_payment = (0.05 * 500000) + (0.1 * (purchase_price - 500000))
else:
    min_down_payment = purchase_price * 0.2
min_down_payment = int(min_down_payment)

print(f"The minimum down payment allowed is ${min_down_payment}")

# Determine down payment percentage
down_payment_percentage = (min_down_payment / purchase_price) * 100

# Input desired percentage for down payment
chosen_perc = input(f"Enter down payment percentage (minimum 5.000): ")
chosen_perc = float(chosen_perc)
if chosen_perc < 5:
    print("Error: Minimum down payment percentage is 5.000")
    exit()

down_payment = purchase_price * (chosen_perc / 100)

# Calculate insurance cost based on the chosen percentage
if 5 <= chosen_perc < 10:
    insurance_cost = (purchase_price - down_payment) * (4 / 100)
elif 10 <= chosen_perc < 15:
    insurance_cost = (purchase_price - down_payment) * (3.1 / 100)
elif 15 <= chosen_perc < 20:
    insurance_cost = (purchase_price - down_payment) * (2.8 / 100)
else:
    insurance_cost = 0

# Calculate the principal amount
principal_amount = purchase_price - down_payment + insurance_cost

print(f"Down payment amount is ${down_payment:,.3f}")
print(f"Mortgage insurance price is ${insurance_cost:,.2f}")
print(f"Total mortgage amount is ${principal_amount:,.2f}")

#Mortgage Term and Amortization Period
mortgageTerm = int(input("Enter mortgage term (1, 2, 3, 5, 10): "))
amortizationPer = int(input("Enter mortgage amortization period (5, 10, 15, 20, 25): "))

#Mortgage Interest Rates
mortgageInterestRates = {
    1: 5.95,
    2: 5.9,
    3: 5.6,
    5: 5.29,
    10: 6
}

#retrieve the applicable interest rate
annualInterest = mortgageInterestRates.get(mortgageTerm)
print(f"Interest rate for the term will be {annualInterest:.2f}%")

#calculate effective monthly rate ***(EMR = ((1 + A/2)2)1/12 - 1)***
monthlyRate = ((1 + (annualInterest / 200)) ** 2) ** (1 / 12) - 1

#alculate Number of monthly payments
monthly_payments = amortizationPer * 12
monthly_payment = principal_amount * (monthlyRate / (1 - (1 + monthlyRate) ** -monthly_payments))
print(f"Monthly payment amount is: ${monthly_payment:.2f}")

# print out the amortization achedule
print("\nMonthly Amortization Schedule")
print("Month    Opening Bal        Payment      Principal       Interest    Closing Bal")

opening_balance = principal_amount
for month in range(1, monthly_payments + 1):
    interest_payment = opening_balance * monthlyRate
    principal_payment = monthly_payment - interest_payment
    closing_balance = opening_balance - principal_payment

    print(f"{month:4}      {opening_balance:11.2f}        {monthly_payment:8.2f}         {principal_payment:9.2f}      {interest_payment:11.2f}      {closing_balance:10.2f}")

    opening_balance = closing_balance
