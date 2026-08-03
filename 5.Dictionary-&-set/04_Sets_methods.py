# =========================
# PYTHON SET METHODS
# =========================

# add(x)                    -> Adds an element to the set
# update(iterable)          -> Adds multiple elements from another iterable
# remove(x)                 -> Removes an element (Error if not found)
# discard(x)                -> Removes an element (No error if not found)
# pop()                     -> Removes and returns a random element
# clear()                   -> Removes all elements
# copy()                    -> Returns a shallow copy

# union(set2)               -> Returns union of two sets (|)
# intersection(set2)        -> Returns common elements (&)
# difference(set2)          -> Returns elements in first set only (-)
# symmetric_difference(s2)  -> Returns elements in either set but not both (^)

# intersection_update(s2)   -> Updates set with common elements
# difference_update(s2)     -> Removes elements found in another set
# symmetric_difference_update(s2)
#                           -> Updates set with symmetric difference

# issubset(set2)            -> True if current set is a subset
# issuperset(set2)          -> True if current set is a superset
# isdisjoint(set2)          -> True if both sets have no common elements

# =========================
# COMMON SET OPERATIONS
# =========================

# len(set)                  -> Number of elements
# x in set                  -> Checks if element exists
# x not in set              -> Checks if element doesn't exist
# set1 | set2               -> Union
# set1 & set2               -> Intersection
# set1 - set2               -> Difference
# set1 ^ set2               -> Symmetric Difference


s = {1,5,32,5,5,54,5,5,5,5}

print(s,type(s))

s.add(5666)

print(s,type(s))

s.remove(1)

print(s,type(s))