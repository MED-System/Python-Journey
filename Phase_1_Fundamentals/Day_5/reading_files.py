# Open the file in 'r' (Read) mode to access its content
employee_file = open("employees.txt", "r")
# .readlines() takes all lines in the file and puts them into a List
for employee in employee_file.readlines():
    print(employee)

# Always close the file
employee_file.close()