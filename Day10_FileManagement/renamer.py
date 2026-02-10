import os

# Create a file
with open("old_name.txt", "w") as f:
    f.write("Renaming test")

# Rename the file
if os.path.exists("old_name.txt"):
    os.rename("old_name.txt", "new_name.txt")
    print("File renamed from old_name.txt to new_name.txt")