print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percentage  = input("What percentage tip would you like ti give? 10, 12, or 15? ")
people_no = int(input("How many people to split the bill? "))
tip = (int(tip_percentage) / 100) * bill
share =  round((bill + tip) / people_no,2)
share = "{:.2f}".format(share)
print(f"Each person should pay: ${share}")

