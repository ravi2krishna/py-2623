# Nested Conditionals
# where the inner condition is only checked, if the outer condition is true. 

if True:
    print("1")

if True:
    print("2 - This is Not Nested Condition")

print("======================")
    
if True: # Outer Condition 
    print("1")
    if True: # Inner Condition
        print("2 - This is Nested Condition")
        
print("======================")

if False: # Outer Condition 
    print("1") # Code is not analyzed because condition is statically evaluated as false
    if True: # Inner Condition
        print("2 - This is Nested Condition")
        
print("======================")

# Nested Conditional Use Case 
age = int(input("Enter Your Age: "))
if age >= 18: # True 
    has_id = input("Do You Have Any ID (yes/no): ")
    if has_id == "yes": 
        print("You Can Vote")
    else:
        print("You Cannot Vote Without ID")
else:
    print(f"You Are Too Young To Vote, Just {age} Not Allowed")  
    

# Net Banking Login -> User Authentication -> OTP Authorization

