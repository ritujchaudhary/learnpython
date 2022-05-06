#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to tip calculator")

total_bill = input("what was the total bill for? ")
tip_percent = input("what is the tip % 10,12 or 15 ? ")

total_bill = float(total_bill) + float(total_bill)*float(tip_percent)/100

split_bill = input("how manu people want to split")

eachbill = round(total_bill/float(split_bill) , 2)

##formating to exact 2 decimal places 34.50 instead of 34.5 (round function will ignore the zero)

eachbill = "{:.2f}".format(eachbill)
print(f"each person should pay {eachbill} ")

