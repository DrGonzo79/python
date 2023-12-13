value = 1
while value <= 10:
    print(value)
    if value == 5:
        break
    value += 1

print("***********************")

while value <= 10:
    value += 1
    if value == 1:
        continue
    print(value)
else:
    print("Value is now equal to " + str(value))
