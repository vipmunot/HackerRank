mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())
tip = mealCost * (tipPercent/100)
tax = mealCost * (taxPercent/100)
totalCost = mealCost + tip + tax
totalCost = round(totalCost)
print ("The total meal cost is %s dollars."%totalCost)