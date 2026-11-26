# Looping Structures (Iteration Statements) (Repetitions)

# while loop

while False: # Code is not analyzed because condition is statically evaluated as false
    print("Repeat....")
    print("Code..............")
    
# while True: 
#     print("Repeat....")
#     print("Code..............")

# To Terminate Above Loop Use Control + c 

# Counters 
count = 1
while count <= 10: 
    print(f"Count Is {count}")
    count += 1
    
print("===================")

# Generate 5k Employee ID's Start With 10001 - 15000
emp_id = 10001
while emp_id <= 15000:
    print(f"Employee ID Generated: {emp_id}")
    emp_id += 1

print("===================")

# use while loop, when we don't know number of Iterations/Repetitions in advance

# You Found A Lost Phone, Trying To Break PIN / Password 
# Tell Me At Which Attempt, The Phone Will Be Unlocked ?? 

actual_pin = "2345"
user_given_pin = ""

while user_given_pin != actual_pin:
    user_given_pin = input("Enter PIN To Unlock: ")
print("Phone Unlocked")

print("===================")

# For Loop 
prices_products = [1000,1500,2000,2500,100000]

# Requirement: Some Offer is running -> Provide a discount of 250 on each product 
print("=================== Prices Before Discount ===================")
print(prices_products)
# In Lists, We Have Index, Which Starts From 0 and Keeps Incrementing
print(prices_products[0])
print(prices_products[1])
# . 
# . 
# . 
# . 

print("=================== Prices After Discount ===================")
print(prices_products)
# In Lists, We Have Index, Which Starts From 0 and Keeps Incrementing
print(prices_products[0] - 250)
print(prices_products[1] - 250)
# . 
# . 
# . 
# print(prices_products[14999] - 250)

# Say We Have 15k Products 

# Using For Loop
prices_products = [1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,100000]
print("=================== Prices Before Discount ===================")
for price in prices_products:
    print("Price Before Discount: ",price)
    
print("=================== Prices After Discount ===================")
for price in prices_products:
    print("Price Before Discount: ",price - 250)
    
print("===================")    

# without range() function 
nums = [1,2,3,4,5,6,7,8,9,10,11,12] # 100 is difficult
for num in nums:
    print(num)

print("===================")    

# range(start, stop, step)
for num in range(1,101,1):
    print(num)

print("===================") 

for num in range(5,101,5):
    print(num)
 
print("===================")  
    
# prices_products = [1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,100000]
for price in range(1000,100500,500):
    print("Price Of Product: ",price)
    
print("===================") 