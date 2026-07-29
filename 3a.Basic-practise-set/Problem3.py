# 3. Write a program to detect double space in a string.  

a = "Shubh is   here to  eat appples  "

b = a.endswith("  ")
c = a.count("  ")
print(b)
print(c)