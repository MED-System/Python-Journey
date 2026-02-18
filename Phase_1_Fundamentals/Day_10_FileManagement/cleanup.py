import os

# Create a file
with open("trash.txt", "w") as f:
    f.write("This will be deleted")

# Check and delete
if os.path.exists("trash.txt"):
    os.remove("trash.txt")
    print("trash.txt successfully removed")