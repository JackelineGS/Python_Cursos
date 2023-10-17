# CLASE 2 
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
a = float(weight)
b = float(height)

bmi = a/(b*b) # a/b**2
bmi = int(bmi)
print(bmi)



age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
# Calculemos el número de días que nos queda

# Tomamos la entrada como edad 
a = int(age)
# Realizamos la operación para saber cuantas semanas hay en un año
live = (90 - a)*52
# Mostramos la respuesta usando print 
print(f"You have {live} weeks left.")


#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome the tip calculator.")
qt = float(input("Whath was the total bill?  $"))
percent = int(input("What percentage tip would like to give?" + " 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

result = (qt * (1 + percent / 100)) / people
# new_result = round(result, 2)
new_result = "{:.2f}".format(result)
print(f"Each person should pay: ${new_result}")
















