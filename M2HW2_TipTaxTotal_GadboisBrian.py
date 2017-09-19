# CTI-110 
# M2HW2 - Tip Tax Total 
# Brian Gadbois
# 9/19/2017
# A program made to figure out your total bill


# foodCost
# tipAmount
# salesTax
# totalCost


tipAmount = .18
salesTax = .07

# What is cost of food
foodCost = float(input ('What is the price of your meal: $'))

# What is the sales tax
tax = foodCost * salesTax
print ('Your tax will be: $', tax)

# What is the tip going to be
tip = foodCost * tipAmount
print ('The amount for tip will be: $', tip)

# What is the the total
totalCost = foodCost + tip + tax
print ('Your total will be : $', totalCost)

