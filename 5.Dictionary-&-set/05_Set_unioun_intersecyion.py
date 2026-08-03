# ==========================
# PYTHON SET (REFERENCE)
# ==========================

# A Set is an unordered collection of unique elements.

# ==========================
# CREATING A SET
# ==========================

# {1, 2, 3}          -> Creates a set
# set()              -> Creates an empty set
# {}                 -> Creates an empty dictionary (NOT a set)

# ==========================
# PYTHON SET METHODS
# ==========================

# add(x)                         -> Adds a single element
# update(iterable)               -> Adds multiple elements
# remove(x)                      -> Removes an element (Error if absent)
# discard(x)                     -> Removes an element (No Error if absent)
# pop()                          -> Removes and returns a random element
# clear()                        -> Removes all elements
# copy()                         -> Returns a shallow copy

# union(set2)                    -> Returns union of two sets
# intersection(set2)             -> Returns common elements
# difference(set2)               -> Returns elements in first set only
# symmetric_difference(set2)     -> Returns non-common elements

# intersection_update(set2)      -> Keeps only common elements
# difference_update(set2)        -> Removes common elements
# symmetric_difference_update()  -> Updates with non-common elements

# issubset(set2)                 -> Checks if subset
# issuperset(set2)               -> Checks if superset
# isdisjoint(set2)               -> Checks if no common elements

# ==========================
# COMMON SET OPERATIONS
# ==========================

# len(set)           -> Returns number of elements
# x in set           -> Checks if element exists
# x not in set       -> Checks if element does not exist
# for x in set       -> Iterates through a set

# set1 | set2        -> Union
# set1 & set2        -> Intersection
# set1 - set2        -> Difference
# set1 ^ set2        -> Symmetric Difference

# ==========================
# IMPORTANT NOTES
# ==========================

# Sets do NOT allow duplicate values.
# Sets are unordered.
# Sets are mutable.
# Set elements must be immutable (int, str, tuple, etc.).
# Sets do not support indexing or slicing.
# Use set() to create an empty set.
# {} creates an empty dictionary.

s1 = {1,3,24,55,78,32,11}
s2 = {3,2,55,66,34,11,23,53,64,1,45,3,85,7}

print(s1.union(s2))
print(s1.intersection(s2))
print(s1 - s2)
print(s2 ^ s1)