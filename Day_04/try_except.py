## Shield that prevents the program from crashing if the user makes a mistake
try:
    number = int(input("enter a number: "))
    print(number)
except ZeroDivisionError:
    print("division by zero")
except ValueError:
    # This is for when someone types 'abc' instead of '123'
    print("invalid input")