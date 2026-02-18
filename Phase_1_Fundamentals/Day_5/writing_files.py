# 'a' (Append) adds "Toby" to the end of file
employee_file = open("employees.txt", "a")
employee_file.write("\nToby - Human Resources")
employee_file.close()

# 'w' writes: It erases EVERYTHING and starts a brand-new file.
# If the file name is new, it just creates it for you.
web_file = open("index.html", "w")
web_file.write("<html><body></body></html>")
web_file.close()