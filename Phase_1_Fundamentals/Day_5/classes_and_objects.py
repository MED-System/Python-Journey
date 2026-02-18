# 'from Student' looks for the file Student.py
# 'import Student' brings in the specific Class defined in that file
from student import Student

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("pam", "Art", 2.5, True)
print(student1.name)
print(student2.name)