
# ================= PYTHON STRING FUNCTIONS =================
# function name        function work                     return type    syntax
# len(s)              -> Length of string                  -> int       -> len(s)
# lower()             -> Convert to lowercase              -> str       -> s.lower()
# upper()             -> Convert to uppercase              -> str       -> s.upper()
# capitalize()        -> First letter uppercase            -> str       -> s.capitalize()
# title()             -> Capitalize every word             -> str       -> s.title()
# swapcase()          -> Reverse letter case               -> str       -> s.swapcase()
# casefold()          -> Aggressive lowercase              -> str       -> s.casefold()
#
# strip()             -> Remove spaces (both ends)         -> str       -> s.strip()
# lstrip()            -> Remove left spaces                -> str       -> s.lstrip()
# rstrip()            -> Remove right spaces               -> str       -> s.rstrip()
#
# replace()           -> Replace substring                 -> str       -> s.replace(old, new)
# find()              -> First index (-1 if absent)        -> int       -> s.find(sub)
# rfind()             -> Last index (-1 if absent)         -> int       -> s.rfind(sub)
# index()             -> First index (error if absent)     -> int       -> s.index(sub)
# rindex()            -> Last index (error if absent)      -> int       -> s.rindex(sub)
# count()             -> Count occurrences                -> int       -> s.count(sub)
#
# startswith()        -> Check prefix                      -> bool      -> s.startswith(prefix)
# endswith()          -> Check suffix                      -> bool      -> s.endswith(suffix)
#
# split()             -> Split into list                   -> list      -> s.split(sep)
# rsplit()            -> Split from right                  -> list      -> s.rsplit(sep)
# splitlines()        -> Split by newlines                 -> list      -> s.splitlines()
# join()              -> Join iterable into string         -> str       -> sep.join(iterable)
# partition()         -> Split into 3 parts                -> tuple     -> s.partition(sep)
# rpartition()        -> Split from right into 3 parts     -> tuple     -> s.rpartition(sep)
#
# center()            -> Center align                      -> str       -> s.center(width)
# ljust()             -> Left align                        -> str       -> s.ljust(width)
# rjust()             -> Right align                       -> str       -> s.rjust(width)
# zfill()             -> Pad leading zeros                 -> str       -> s.zfill(width)
#
# isalpha()           -> Only alphabets?                   -> bool      -> s.isalpha()
# isdigit()           -> Only digits?                      -> bool      -> s.isdigit()
# isnumeric()         -> Only numeric chars?               -> bool      -> s.isnumeric()
# isdecimal()         -> Only decimal digits?              -> bool      -> s.isdecimal()
# isalnum()           -> Alpha + numeric only?             -> bool      -> s.isalnum()
# islower()           -> All lowercase?                    -> bool      -> s.islower()
# isupper()           -> All uppercase?                    -> bool      -> s.isupper()
# istitle()           -> Title case?                       -> bool      -> s.istitle()
# isspace()           -> Only whitespace?                  -> bool      -> s.isspace()
# isascii()           -> ASCII characters only?            -> bool      -> s.isascii()
# isidentifier()      -> Valid Python identifier?          -> bool      -> s.isidentifier()
# isprintable()       -> Printable characters only?        -> bool      -> s.isprintable()
#
# format()            -> Format string                     -> str       -> s.format(args)
# format_map()        -> Format using mapping              -> str       -> s.format_map(dict)
# encode()            -> Convert to bytes                  -> bytes     -> s.encode()
# expandtabs()        -> Replace tabs with spaces          -> str       -> s.expandtabs(tabsize)
# ===========================================================
# 
# 
# # 1. len () function – This function returns the length of the strings. 
str = "shubh" 
print(len(str))  # Output: 5 

# 2. String.endswith("rry") – This function_ tells whether the variable string ends with 
# the string "rry" or not. If string is "harry", it returns true for "rry" since Harry ends 
# with rry. 

print(str.endswith("ubh"))#returns true
print(str.endswith("ubham"))#returns false

# 3. string.count("c") – counts the total number of occurrences of any character. 

count = str.count("h") 
print(count)  # Output: 2 

count = str.count("y") 
print(count)  #Output 0

# 4. the first character of a given string.

capitalized_string = str.capitalize() 
print(capitalized_string)  # Output: "Shubh"

# 5. string.find(word) – This function friends a word and returns the index of first 
# occurrence of that word in the string. 

index = str.find("bh") 
print(index)  # Output: 3

# 6. string.replace (old word, new word ) – This function replace the old word with 
# new word in the entire string. 

replaced_string = str.replace("u", "#") 
print(replaced_string)  # Output: Sh#bh