# Tutorial Assignment: Lists, Sets, and Dictionaries in Python

# List operations
my_list = [1, 2, 3]
print("Original list:", my_list)

# Adding elements
my_list.append(4)
print("After appending 4:", my_list)

# Removing elements
my_list.remove(2)
print("After removing 2:", my_list)

# Accessing elements
print("Element at index 1:", my_list[1])

print("\n---\n")

# Set operations
my_set = {1, 2, 3}
print("Original set:", my_set)

# Adding elements
my_set.add(4)
print("After adding 4:", my_set)

# Removing elements
my_set.discard(2)
print("After discarding 2:", my_set)

# Accessing elements (sets are unordered, so we check membership)
print("Is 3 in set?", 3 in my_set)

print("\n---\n")

# Dictionary operations
my_dict = {"a": 1, "b": 2, "c": 3}
print("Original dictionary:", my_dict)

# Adding elements
my_dict["d"] = 4
print("After adding key 'd':", my_dict)

# Removing elements
del my_dict["b"]
print("After deleting key 'b':", my_dict)

# Accessing elements
print("Value for key 'a':", my_dict.get("a"))
