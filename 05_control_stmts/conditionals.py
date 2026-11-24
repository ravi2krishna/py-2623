# Conditional Structures (Decision Making Statements)

# if 

if True:
    print("This")
    print("Is")
    print("Block")
    print("Of")
    print("Code")
    
print("=====================")

if False: # Code is not analyzed because condition is statically evaluated as false
    print("This")
    print("Is")
    print("Block")
    print("Of")
    print("Code")
    

if 5 > 2:
    print("Old")
    print("Is")
    print("Block")
    print("Of")
    print("Code")

print("=====================")
    
if 1 > 2:
    print("New")
    print("Is")
    print("Block")
    print("Of")
    print("Code")
   
print("=====================")
 
num = -5 
if num > 0:
    print("Given Num Is Positive")
if num < 0:
    print("Given Num Is Negative")   

print("=====================")
    
# if else 
num = 1
if num > 0:
    print("Given Num Is Positive")
else:
    print("Given Num Is Negative")
    
print("=====================")

# without input() - Data Is Hardcoded i.e Static 
person_name = "Ravi"
print("Welcome: "+person_name) 

print("=====================")

# with input() - Data Is Dynamic i.e Changes 
username = input("Enter Your Username: ")
print("Welcome: "+username) 
print("Welcome: ",username) 
print("Welcome: {username}") 
print(f"Welcome: {username}") # interpolation

print("=====================")

# if else 
num = input("Enter Number: ")
num = int(num)
if num > 0: # TypeError: '>' not supported between instances of 'str' and 'int'
    print(f"Given Number {num} Is Positive")
else:
    print(f"Given Number {num} Is Negative")