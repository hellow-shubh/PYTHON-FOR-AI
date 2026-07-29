# 2. Write a program to fill in a letter template given below with name and date. 
# letter = '''  
#        Dear <|Name|>, 
#        You are selected! 
#        <|Date|> 
#         ''' 
 



letter = '''  
        Dear <|Name|>, 
        You are selected! 
        <|Date|> 
         ''' 

name = str(input("Enter name: "))
date = str(input("Enter date: "))

letter = letter.replace("<|Name|>",name)
letter = letter.replace("<|Date|>",date)
print(letter)