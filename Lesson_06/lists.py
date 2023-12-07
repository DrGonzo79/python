users = ['Dave', 'John', 'Johnny', 'Alice']

data = ['John', 42, True]

emptylist = []

users.append('Justin')
users += ['Jason', 'Sheila', 'Ryan']
users.extend(['Juan', 'Juanita'])
# users.extend(data) # not a good combination of mixed values
users.insert(2, 'Bobby')
users[2:2] = ['Jen', 'Misty']  # insert: names at position 2 and end at 2
users[1:3] = ['JPJ']  # slice: starting at position 1 and end at 3
users.remove('JPJ')
print('Pop example: ' + str(users))
print(users.pop())
del users[0]

print('')
print('1: ' + str(users[2]))  # casting int to str for concat
print('')
print('2: ' + str(users[-2]))
print('')
print('Index Position of Johnny: ' + str(users.index('Johnny')))
print('')
# casting list to a string to create a concatenated string
print('Data length: ' + str(len(users)))
print('')
print('User Names: ' + str(users))
print('')
print('Data list: ' + str(data))
data.clear()
print('Cleared data list: ' + str(data))

# sorting lists
# lower case gets sorted after strings that begin with upper
users[5:5] = ['albert']
users.sort()
print(users)
users[5:5] = ['Albert']  # uppercase gets sorted with equal str but before lower
users.sort(key=str.lower)
print('Sort using both upper and lower: ' + str(users))

nums = [4, 42, 58, 44, 12, 12]
nums.reverse()  # reverses original array
print('Nums list: ' + str(nums))

nums.sort(reverse=False)
print('Nums list: ' + str(nums))
# Global sorted function does not modify original array
print(sorted(nums, reverse=True))
print(nums)  # showing original list was not modified

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print('')
print(numscopy)
mynums.sort(reverse=True)
print(mynums)
print(mycopy)
print(nums)
print('')
print(type(nums))
print(type(mynums))
print('')

print(type(nums))
mylist = list([1, "Neil", True])
print(mylist)

# Tuples
mytuple = tuple(("Dave", 42, True))

anothertuple = (1, 4, 2, 8, 2, 2)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append("neil")
newtuple = tuple(newlist)
print(newtuple)

print('')
print("TUPLES")
(one, *two, hey) = anothertuple
print(one)
print(two)
print(hey)

print("Tuple Count: " + str(anothertuple.count(4)))
