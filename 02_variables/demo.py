# Variables

# Assign Data (Store Data)
student_name = "Ravi" # string
student_age = 25 # int 
student_passed = True # Correct (Student has passed) # bool
student_failed = False # In Correct # bool 
STUDENT_AADHAR = None # Absence Of Value # NoneType

# Retrieve Data (Get Data)
# type()
print(student_name)
print(type(student_name))

print(student_age)
print(type(student_age))

print(student_passed)
print(type(student_passed))

print(student_failed)
print(type(student_failed))

print(STUDENT_AADHAR)
print(type(STUDENT_AADHAR))



# Concatenation: Joining Strings Using + Operator
print("============ Student Information ============")
# print("Student Name: John")
print("Student Name: " + student_name)
# print("Student Age: " + student_age) # TypeError: can only concatenate str (not "int") to str
print("Student Age: ",student_age)
print("Did Student Pass: ",student_passed)
print("Did Student Fail: ",student_failed)
print("Student Aadhar ID: ",STUDENT_AADHAR)
print("============ Student Information ============")


# id()
print(id(student_name))
print(id(student_age))
print(id(student_passed))
print(id(student_failed))
print(id(STUDENT_AADHAR))

print("========================")

# Memory Model In Python 
value_x = 10
print(id(value_x))

value_y = 100
print(id(value_y))

value_z = 10
print(id(value_z))
