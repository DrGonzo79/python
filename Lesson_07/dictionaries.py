# Dictionaries
band = {
    "vocals": "Robert Plant",
    "guitar": "Jimmy Page",
}

band2 = dict(vocals="Robert Plant", guitar="Jimmy Page")

print(band)
print(band2)
print(type(band))
print(len(band))

# Access Items
print(band["vocals"])
print(band.get("guitar"))

# list all keys
print(band.keys())

# list all values
print(band.values())

# list of key value pairs as tuples
print(band.items())

# verify a key exists
print("guitar" in band)
print("triangle" in band)

# Change Values
band["guitar"] = "Eric Clapton"
band.update({"bass": "JPJ"})
print(band)
print("------------------")

# Remove items
print(band.pop("bass"))
print(band)

band["drums"] = "Bohnam"
print(band)

print(band.popitem())  # tuple
print(band)

# delete and clear

band["drums"] = "Bohnam"
del band["drums"]
print("------------------")
print(band)

band2.clear()
print(band2)
del band2

# copy dictionaries
# band2 = band  # create a reference
# print("Bad copy!")
# print(band2)
# print(band)

# band2["drums"] = "Dave"
# print(band)

band2 = band.copy()
band2["drums"] = "Dave"
print("**************")
print("Good copy!")
print(band)
print(band2)

# or use the dict() constructor function
band3 = dict(band)
print("Good copy!")
print(band3)

# Nested Dictionaries
member1 = {
    "name": "Plant",
    "instrument": "vocals"
}
member2 = {
    "name": "Page",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}

print("$$$$$$$$$$$$$$$$$$")
print(band)
print(band["member1"]["name"])

# Sets
nums = {1, 2, 3, 4, 5, 6, 7, 8, 9}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

# no duplicates allowed
nums = {1, 2, 2, 4, 5, 6, 7, 8, 9, 1}
print(nums)

# True is a dupe of 1, False is a dupe of 0
nums = {1, True, 2, False, 3, 4, 5, 6, 7, 8, 9, 0}
print(nums)

# check if a value is in a set
print(1 in nums)

# but you cannot refer to an element in the set with an index position or a key

# add a new element to a set
nums.add(10)
print(nums)

# Add elements from one set to another
morenums = {11, 12, 13, 14, 15}
nums.update(morenums)
print(nums)

# you can use update with lists, tuples, and dictionaries, too.

# merge two sets to create a new set
one = {1, 2, 3}
two = {4, 5, 6}

mynewset = one.union(two)
print("**************")
print(mynewset)

# keep only the duplicates
one = {1, 2, 3}
two = {2, 3, 6}

one.intersection_update(two)
print("Duplicates: " + str(one))

# keep everything but the duplicates
one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)
