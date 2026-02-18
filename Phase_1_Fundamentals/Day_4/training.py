# Convert input string to a decimal number
reading = float(input("enter the sensor reading: "))

# Check for critical temperature
if reading >= 100:
    print("Danger: Overheating")
# Check for caution zone (between 50 and 100)
elif reading > 50:
    print("Warning: High Temp")
# Everything else (50 or below)
else:
    print("System OK")