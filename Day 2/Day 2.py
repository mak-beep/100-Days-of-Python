print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, 15 "))
tip_percentage = tip/100
total_tip = tip_percentage*bill
total_amount = bill+total_tip
pay_per_person = total_amount/people
rounded_Pay = round(pay_per_person,2)
# An alternative to fix / limit decimal places.
rounded_Pay = "{:.2f}".format(pay_per_person)
print(f"Each person should pay: ${rounded_Pay}")