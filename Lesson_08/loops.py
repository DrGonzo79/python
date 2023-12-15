value = 1
while value <= 10:
    print(value)
    if value == 5:
        break
    value += 1

print("***********************")

# while value <= 10:
#     value += 1
#     if value == 1:
#         continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value))

names = ["John", "Mary", "Bob"]
# for x in names:
#     print(x)

# for x in "Mississippi":
#     print(x)

# for x in names:
#     if x == "Mary":
#         break
#     print(x)

# for x in names:
#     if x == "Mary":
#         continue
#     print(x)

# for x in range(4):
#     print(x)

# for x in range(5, 101, 5):
#     print(x)
# else:
#     print("Done son!")

names = ["John", "Mary", "Bob"]
actions = ["ran", "ate", "walked"]

# for name in names:
#     for action in actions:
#         print(name + " " + action)

for action in actions:
    for name in names:
        print(name + " " + action)
