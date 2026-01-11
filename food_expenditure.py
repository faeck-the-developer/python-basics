num1 = float(input("How many times a week do you eat at the student cafeteria? "))
num2 = float(input("The price of a typical student lunch? "))
num3 = float(input("How much money do you spend on groceries in a week? "))
weekly = (num1 * num2) + num3 
daily = (weekly / 7)
print ("Average food expenditure:")
print(f"Daily: {daily:.1f} euros")
print(f"Weekly: {weekly:.1f} euros")
