print("Welcome to Tip Calculator.")
bill_amount = float(input("What is the bill amount? $"))
tip_percent = int(input("What is the percentage of tip you want to give? 10, 12 or 15? "))
number_of_person = int(input("How many people to split the bill? "))
total_per_person = (bill_amount + (bill_amount*tip_percent/100))/number_of_person
print(f"Each person should pay : ${round(total_per_person, 2)}")