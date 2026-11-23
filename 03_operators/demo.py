# Arithmetic Operators 

num1 = 10
num2 = 5

print("Sum Of Numbers: ",num1 + num2)
print("Difference Of Numbers: ", num1 - num2)
print("Product Of Numbers: ",num1 * num2)
print("Division Of Numbers: ",num1 / num2)

print("Floor Division Of Numbers: ",num1 // num2)

print("Exponentiation: ",num1 ** num2) # 10 ^ 5 
print("Exponentiation: ",3 ** 2) # 3 ^ 2

print("=============================")

# Compound Assignment Operators 
num = 10
num = num + 5 # long form
print(num)

num = 10
num += 5 # short form
print(num)

# Increment & Decrement Operators
count = 1
print(count)
# count++ # SyntaxError: invalid syntax
count += 1
print(count)
count += 1
print(count)
count += 1
print(count)


count = 10
print(count)
count -= 1
print(count)
count -= 1
print(count)
count -= 1
print(count)

print("=============================")

# Comparison Operators
num1 = 5
num2 = 2 

print(num1 > num2)
print(num1 < num2)
print(num1 == num2)

print("=============================")

# Logical Operators 
num1 = 4
num2 = 3
num3 = 2
num4 = 1

print(num1 > num3 and num3 > num4) # T and T -> T
print(num1 > num3 and num3 < num4) # T and F -> F

print(num1 > num3 or num3 > num4) # T or T -> T
print(num1 > num3 or num3 < num4) # T or F -> T

print(num1 > num3) # T
print(not num1 > num3) # T -> F

print("=============================")

# Membership Operators 
data = "python is programming language"
find_word = "java"

status = find_word in data
print(status)

data = "python is programming language"
find_word = "python"

status = find_word in data
print(status)

# List Data Type -> It consists of multiple values, we use [] to define lists
employee_ids = [101,102,103,105,107,108,109,110]
find_emp_id = 103
status = find_emp_id in employee_ids
print("Employee Found: ",status)

find_emp_id = 106
status = find_emp_id in employee_ids
print("Employee Found: ",status)

find_emp_id = 106
status = find_emp_id not in employee_ids
print("Employee Not Found: ",status)

print("=============================")

# Identity Operators 

n1 = 10
n2 = 10
n3 = 50

print (n1 is n3) # False 
print (n1 is n2) # True
print(id(n1)) 
print(id(n2)) 
print(id(n3)) 

print("=============================")

# Bitwise Operators 
n1 = 5 # 00000101
n2 = 3 # 00000011
       # 00000001 - &
       # 00000111 - |
       


print(n1 & n2) # 1
print(n1 | n2) # 7 
