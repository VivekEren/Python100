"""
Program to calculate tip
total amount is the addition of total bill and amount of the tip that needs to be given
tip is calculated by multiplying total bill with tip percentage and dividing by 100
each person expense is total amount divided by total number of people and round the expense upto two decimal points
"""
print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? $"))
tip_percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))
total_amount = total_bill + (total_bill * tip_percentage/100)
each_person_amount = round(total_amount / total_people, 2)
print(f"Each person should pay: ${each_person_amount}")
