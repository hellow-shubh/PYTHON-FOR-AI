# ==========================
# PYTHON DICTIONARY METHODS
# ==========================

# clear()        -> Removes all items
# copy()         -> Returns a shallow copy
# fromkeys()     -> Creates dictionary from given keys
# get()          -> Returns value of a key (safe access)
# items()        -> Returns key-value pairs
# keys()         -> Returns all keys
# values()       -> Returns all values
# pop()          -> Removes specified key
# popitem()      -> Removes last inserted key-value pair
# setdefault()   -> Returns value; inserts key if absent
# update()       -> Updates dictionary with another dictionary

# Common Dictionary Operations (Not Methods):

# len(dict)      -> Number of key-value pairs
# del dict[key]  -> Deletes a key
# key in dict    -> Checks if key exists
# dict[key]      -> Access value
# dict[key] = v  -> Add/Update key-value pair
marks = {
    "Shubh" : 100,
    "Shubham" : 80,
    "Shubhankar" : 10,
    0 : "Shubh"
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Shubh" : 99, "Divya" : 99})
print(marks)
print(marks.get("Shivika"))
print(marks.get("Shubh"))
# print(marks.get("Shubh")) aur marks ["SHubh"] me antar kya hoga????
#it is in output which is as follows
print(marks.get("Shubh2"))#returns none
print(marks["Shubh2"])#returns error 