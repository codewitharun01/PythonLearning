list = ["Arun", "Asha", "Kichu"]
tuple = ("Arun", "Asha", "Kichu")
set = {"Arun", "Asha", "Kichu"}

# Access individual items in lists and tuples using the index.

print(list[0])
print(tuple[0])
# print(set[0])  # This gives an error because sets are unordered, so accessing element 0 of something without order doesn't make sense.

# Modify individual items in lists using the index.

list[0] = "Das"
# t[0] = "Smith"  # This gives an error because tuples are "immutable".

print(list)
print(tuple)

# Add to a list by using `.append`

list.append("Kiran")
print(list)
# Tuples cannot be appended to because they are immutable.

# Add to sets by using `.add`

set.add("Sindhu")
print(set)

# Sets can't have the same element twice.

set.add("Asha")
print(set)