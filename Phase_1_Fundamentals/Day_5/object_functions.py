from Student1 import Student

student1 = Student("oscar", "accounting", 3.1)
student2 = Student("Pam", "Art", 3.8)

print(student1.on_honor_roll()) # This will print False
print(student2.on_honor_roll()) # This will print True