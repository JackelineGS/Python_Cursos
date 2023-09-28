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

question_one = input("¿Cómo se llama la ciudad donde naciste? ")

question_two = input("¿Cómo se llama tu mascota? ")

print("El nombre de tu banda es: " + question_one + " " + question_two)








