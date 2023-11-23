import math

# String Data Type

# Literal Assignment
first = 'Doctor'
last = 'Gonzo'

# # print('')
# # print(type(first))
# # print(type(first) == int)
# # print(isinstance(first, str))
# # print('')

# # Constructor Function
# # pizza = str('Pepperoni')
# # print(type(pizza))
# # print(type(pizza) == bool)
# # print(isinstance(pizza, str))
# # print('')

# # Concatenation
# fullname = first + " " + last
# print(fullname)

# fullname += '!'
# print(fullname)

# # Casting a number to a string
# decade = str(1980)
# print(type(decade))
# print(decade)

# statement = "I like music from the " + decade + "s."
# print(statement)

# # Multiple lines
# multiline = '''
# Hey how are you.

# I was just checking in.
#             All good?
# '''

# print(multiline)

# # Escaping special characters
# sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'

# print(sentence)

# # String methods
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title())
# print(multiline.replace("good", 'ok'))

# print(len(multiline))
# multiline += "                             "
# multiline = "              " + multiline
# print(len(multiline))

# print('')
# print(len(multiline.strip()))
# print(len(multiline.rstrip()))
# print(len(multiline.lstrip()))

# Build a menu
title = "menu".upper()
# print('')
# print(title.center(20, "="))
# print("Coffee".ljust(16, ".") + "$1".rjust(4))
# print("Muffin".ljust(16, ".") + "$2".rjust(4))
# print("Cheesecake".ljust(16, ".") + "$4".rjust(4))
# print('')

# String Index Values
# print('')
# print(first[1])
# print(first[-1])
# print(first[1:-1])
# print(first[1:])
# print(first[:-1])
# print(first[:])

# Some methods return boolean data
# print(first.startswith("D"))
# print(first.endswith("e"))

# Boolean data type
myValue = True
x = bool(False)
# print(type(x))
# print(isinstance(myValue, bool))

# Numeric data types

# Integer Type
price = 100
bestPrice = int(80)

# print(type(price))
# print(isinstance(bestPrice, bool))

# Float type
gpa = 3.18
y = float(3.45)
# print(type(gpa))
# print(isinstance(y, float))

# Complex type
comp_value = 5+3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)

# Built-in functions for numbers
# print(abs(gpa))

# print(round(gpa))
# print(round(gpa, 1))

# print('')

# print(math.pi)
# print(math.sqrt(64))
# print(math.ceil(gpa))
# print(math.floor(gpa))

# Casting a string to a number
zipcode = '10001'
zip_value = int(zipcode)
# print(type(zip_value))

# Error if you attempt to cast incorrect data
# zip_value = int("New York")
