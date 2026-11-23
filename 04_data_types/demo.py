# Data Types 

# Numeric Types 

data = 100
print(type(data))

data = -10
print(type(data))

data = 10.0
print(type(data))

data = -10.5
print(type(data))

# Complex Number -> a + ib 
# data = 3 + i5 # Error 
# print(type(data))

# Complex Number -> a + bj 
data = 3 + 5j
print(type(data))

# Boolean Types 

data = True
print(type(data))

data = False
print(type(data))

# NoneType

data = None 
print(type(data))

# String Type 
data = 'python'
print(type(data))

data = "python"
print(type(data))

# Complex Data Types 

# List 
data = [10,20,30,40,50]
print(type(data))

size_options = [38,40,42,44,46]
print(type(size_options))

# Tuples
data = (10,20,30,40,50)
print(type(data))

# Sets
data = {10,20,30,40,50}
print(type(data))

# Dictionaries
data = {"id":101,"name":"Ravi","course":"python"}
print(type(data))

# Custom Data Type For Student 
class Student:
    student_id = 101
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    student_contact = 998899889988
    student_gpa = 9.3
    student_enrolled_courses = ["python","sql","django"]
    
data = Student() # Object Creation (OOP)   
print(type(data)) # custom data type 

# Type Conversion / Implicit Conversion [Automatic]
num1 = 10 # int 
num2 = 5.5 # float 
sum = num1 + num2 # float 
print(sum)
print(type(sum))

# Type Casting / Explicit Conversion [Manual]
price = 1128.23 # float 
print(price)
print(type(price))
# Round Off Price 1128 it's int 
# data_type(variable_name)
round_off_price = int(price)
print(round_off_price)
print(type(round_off_price))

