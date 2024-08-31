print("Welcome to the tip calculator\n")
total_bill = float(input("What was the total bill?\n"))

tip = int(input("How much tip would you like to give? %10, %12, or %15\n"))

number_of_person = int(input("How many people to split the bill?\n"))

tip_percent = tip/100
tip_amount = total_bill * tip_percent

per_pound = total_bill / number_of_person + tip_amount /number_of_person

print(f"Each person should pay: £{round(per_pound,2)}")
