# ================================
# PYTHON LIST METHODS (REFERENCE)
# ================================

# append(x)
# -> Adds a single element to the end of the list.

# extend(iterable)
# -> Adds all elements from another iterable to the end of the list.

# insert(index, x)
# -> Inserts an element at the specified index.

# remove(x)
# -> Removes the first occurrence of the specified value.

# pop([index])
# -> Removes and returns the element at the given index.
# -> If no index is provided, removes the last element.

# clear()
# -> Removes all elements from the list.

# index(x[, start[, end]])
# -> Returns the index of the first occurrence of the value.

# count(x)
# -> Returns the number of times a value appears in the list.

# sort(key=None, reverse=False)
# -> Sorts the list in ascending order by default.
# -> Use reverse=True for descending order.

# reverse()
# -> Reverses the order of elements in the list.

# copy()
# -> Returns a shallow copy of the list.
# 


friends = ["Apple","boy",1.45,56,False,"Subh"]
print(friends)
friends.append("shubh choudhary")
print(friends)

l1 = [1,8,7,2,21,15] 
#updates the list to [1,2,7,8,15,21] 
# l1.sort()
# updates the list to [15,21,2,7,8,1] 
# l1.reverse() 
# adds 18 at the end of the list  
# l1.append(18) 
#  This will add 8 at 3 index 
# l1.insert(3,8)
# Will delete element at index 2 and return its value. 
# l1.pop(2)
# Will remove 21 from the list. 
# l1.remove(21)
# print(l1)
