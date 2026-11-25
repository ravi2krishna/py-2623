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

print("=====================")   

# Voting App 
age = int(input("Enter Age: "))
if age >= 18:
    print("You Can Vote")
else:
    print("You Cannot Vote") 

print("=====================")   

# Conditional Expression 
# value_if_true if condition else value_if_false 
age = int(input("Enter Your Age: "))
print("You Can Vote" if age >= 18 else "You Cannot Vote")

print("=====================") 

# Say I Want To Check If Student Passed Or Failed, Passed >= 35 
marks = int(input("Enter Your Marks To Check Passed / Failed: "))
if marks >= 35:
    print("PASSED")
else:
    print("FAILED") 

print("=====================")   

# Check for Grades 
# 90 and above - A Grade
# 75 and above but below 90 - B Grade
# 60 and above but below 75 - C Grade
# 60 and above but below 50 - D Grade
# 35 and above but below 50 - E Grade
# Below 35 Failed 

# elif 

marks = int(input("Enter Your Marks To Check Grade: "))
if marks >= 90: 
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >= 60:
    print("C Grade")
elif marks >= 50:
    print("D Grade")
elif marks >= 35:
    print("E Grade")
else:
    print("FAILED") 
    
print("=====================") 

# match case 
choice = int(input("Enter Your Choice: "))
match choice:
    case 1:
        print("Buy Pizza")
    case 2:
        print("Buy Burger")
    case 3:
        print("Buy Pasta")
    case _:
        print("Only Pizza - Burger - Pasta Available")

print("=====================") 

signal = input("Enter Colour You See: ")
match signal:
    case "red":
        print("Stop Your Vehicle")
    case "orange":
        print("Get Ready To Start")
    case "green":
        print("Move Your Vehicle")
    case _:
        print("Follow Signal")

print("=====================") 