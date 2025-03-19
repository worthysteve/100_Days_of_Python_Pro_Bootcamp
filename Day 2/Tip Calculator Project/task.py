print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))


tip_percent = tip /100
total_tip = bill + bill * tip_percent
total_bill = bill + total_tip
bill_person = total_bill / people
final_amount = round(bill_person, 2)

print(f"Your total bill is ${total_bill} and each person should pay ${final_amount}")


