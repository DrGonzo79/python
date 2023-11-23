# # String Data Type

# # Literal Assignment
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
print('')
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))
print('')

# String Index Values
print('')
print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])
print(first[:-1])
print(first[:])
