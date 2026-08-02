# ================================
# USEFUL TUPLE OPERATIONS
# ================================

# len(tuple)
# -> Returns the number of elements.

# max(tuple)
# -> Returns the largest element.

# min(tuple)
# -> Returns the smallest element.

# sum(tuple)
# -> Returns the sum of all elements (numeric tuples).

# sorted(tuple)
# -> Returns a sorted list (does not modify the tuple).

# tuple(iterable)
# -> Converts an iterable into a tuple.

#  a.count (1): a count (1) will return number of times 1 occurs in a. 
# • a.index (1) will return the index of first occurrence of 1 in a.
 
d=(1,23,243,7654,35,247,5834,12,675)#This will be treated as an tuple also 
print(type(d))
print(len(d))
print(max(d))
print(min(d))
print(sum(d))
print(sorted(d))
print(d.count(675))
print(d.index(12))
