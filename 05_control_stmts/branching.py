# Branching Structures (Jump Statements)

for num in range(1,11,1):
    print(num)
    
print("================")

# break: helps you exit loops
for num in range(1,11,1):
    # stop the loop, when num is 5
    if num == 5: # 20k employees, find emp_id, found 12500 stop here 
        break
    print(num)

print("================")

# continue: helps you skip current Iteration 
for num in range(1,11,1):
    # skip the 5th iteration
    if num == 5: # 20k employees, skip bonus for emp_id 12500
        continue
    print(num)
    
print("================")

# pass: acts as placeholder, does nothing 
# Requirement - To Perform Some Operations In The Future
# When Salary Is Above 25000, We Want To Do Something In Future 
emp_salary = 15000
if emp_salary > 25000:
    pass # _________ # park 
    
# Other Operations To Work On 
print("Working With Next Available Features")

# After 6 Months In The Future
#  When Salary Is Above 25000, We Want To Do Something In Future 
# Something IS Promoted To Permanent Employee 
emp_salary = 35000
if emp_salary > 25000:
    print("Promoted To Permanent Employee ")

# Custom Data Type For Student 
class Student:
    student_id = 101
    student_name = "Ravi"
    student_email = "ravi2krishna@gmail.com"
    student_contact = 998899889988
    student_gpa = 9.3
    student_enrolled_courses = ["python","sql","django"]
    
# Park Some Users 
class Employee:
    pass 

class Manager:
    pass 

class Developer:
    pass 