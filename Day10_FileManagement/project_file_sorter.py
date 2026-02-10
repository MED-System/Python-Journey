#PURPOSE: Move .jpg files into a folder automatically.

import os

#  List names and the folder name
all_files = ["report.txt", "vacation.jpg", "notes.txt", "forest.jpg", "data.csv"]
target_folder = "My_Images"

# Make the files if they don't exist yet
for name in all_files:
    if not os.path.exists(name):
        with open(name, "w") as f:
            f.write("testing")

# Make the folder if it's not there
if not os.path.exists(target_folder):
    os.mkdir(target_folder)

#  Loop through and move only .jpg files
for filename in all_files:
    if filename.endswith(".jpg"):
        old_path = filename
        new_path = f"{target_folder}/{filename}"

        # Only move if the file isn't already in the folder
        if not os.path.exists(new_path):
            os.rename(old_path, new_path)
            print(f"Moved {filename}")
        else:
            print(f"{filename} is already moved")