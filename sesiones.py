
########################################### DAY 1 ###############################################

# Lesson: Printing 
print('Hello Word')
# Exercise 
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# String Manipulation and Code Intelligence

print("Day 1 - Python Print Function \n The function is declared like this: \n print('what to print') ")
print('Hello' + ' Angella')
print('Hello' + ' ' + 'Angella')
 
#Nota: En python tengamos cuidado con la identación. Hay errores de sintaxis y de identación

# The Python Input Function
print('¿What is your name?')
input('¿What is your name?')
print('Hello ' + input('What is your name?'))

# Excersise number 1.3
print(len(input('What is your name? ')))

# Python variables
name = 'Jack'
print(name)

name = 'Angela'
print(name)

# print(len(input('What is your name?'))) 

name = input('What is your name?')
length = len(name)
print(length)

# Excersise number 1.4

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = b
d = a 
a = c 
b = d 

#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)

# Variable naming 
# El código deber ser legible y tener sentido 
# No puedes tener espacios al crear los nombres de las variables
# No puedes colocar números al inicio de la variable
# No usar los nombres restringidos

######################################### DAY 2 ###########################################

# Data Types 

# String 

"Hello"[4] #El resultado es "o"
print("123" + "345")

# Interger 
print(123 + 345)
# Cuando el Python queramos escribir números muy grandes en el que debemos usar comas
# A cambio podemos usar guiones abajo 

123_456_789 

# Float 

3.14159 

# Boolean 
True
False 

# Type Error, Type Checking and Type Conversion 
num_char = len(input('What is your name?'))
print('Your name has' + num_char + ' characters.')
print(type(num_char))

#Convertimos un number en caracter 
new_num_char = str(num_char)

print("Your name has " + new_num_char + " characters.") # Aquí todos los elementos tienen el mismo tipo de data 

# Para saber qué tipo de datos estamos utilizando usamos la función float()
# Para convertir una variable ya existente usamos string, int o float 

a = float(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))






















