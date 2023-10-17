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
















