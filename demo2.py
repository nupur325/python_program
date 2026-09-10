role=input("Enter your role(student/working):")
age=int(input("Enter your age:"))
is_eligible=role.lower()=="student" and age<21
print("Eligible:",is_eligible)