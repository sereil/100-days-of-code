#Tip Calculator
#Day 2 of 100 Days of Code

#Sereil-Vann Phlek - 2022-07-18

#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 /5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: there are 2 ways to round a number. You might have to do some Googling to solve this.

#Write your code below this line.

print("\nWelcome to the tip calculator!\n\n")

bill = float(input("What is the bill?\n"))
num_people = int(input("How many people are splitting the bill?\n"))
tip = int(input("How much tip would you like to give, in %\n"))

split_bill = round((bill/num_people) * (1+tip/100),2)
final_amount = "{:.2f}".format(split_bill)
message = f"Each person should be paying {final_amount}$"
print(message)