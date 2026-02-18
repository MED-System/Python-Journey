## Day 9 Solo Project

filename = "sensor_logs.txt"

try:
    # Open and Read
    with open(filename, "r") as file:
       print(file.read())

    # Get numbers from user
    current_temp = int(input("Please enter your current temperature: "))
    current_time = int(input("Please enter what time it is now: "))

    # Append to write at the end
    with open(filename, "a") as file:
        file.write(f"\n{current_temp}, {current_time}")
        print(f"Recorded temp: {current_temp} at time: {current_time}")

# If file is missing, create it
except FileNotFoundError:
    print("File not found.")
    with open(filename, "w") as file:
        file.write("temp, time")
    print("File created.")

# If user types text instead of number
except ValueError:
    print("Invalid! Use numbers only.")

# Catch any other error
except Exception as e:
    print(f"Error: {e}")