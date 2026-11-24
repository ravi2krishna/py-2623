# Indentation Rules 

# -> When To Use Space -> When We Write Block Of Code

# -> When Not To Use Space -> Single Line Of Statement

# -> How Many Spaces To Use -> At least one space, but recommend is 4 

print("Hello") # Single Line Of Statement

#  print("Hi") # IndentationError: unexpected indent

# Taking class use case for Indentation
# class Student:
# student_name = "Ravi" # IndentationError: expected an indented block after class definition on line 14

# At least one space
class Student:
 student_name = "Ravi" 
 
# two spaces 
class Student:
  student_name = "Ravi" 
  
# ten spaces 
class Student:
          student_name = "Ravi" 
          
# recommend spaces is 4 (tab)
class Student:
    student_name = "Ravi" 
    
# Use "Consistent Number Of Spaces"  
# class Student:
#     student_name = "Ravi" # 4 space 
#   student_email = "ravi@gmail.com"  # 2 space 

class Student:
    student_name = "Ravi"  # 4 space 
    student_email = "ravi@gmail.com" # 4 space 
    

class Student:
 student_name = "Ravi" # 1 space 
 student_email = "ravi@gmail.com"  # 1 space 
 
 