filename = "stock_data.txt"

try:
    # READ the file
    with open(filename, "r") as file:
        print("--- Current Inventory ---")
        print(file.read())

    # GET INPUT
    new_item = input("Add new item name: ")
    new_price = int(input(f"Enter price for {new_item}: "))

    with open(filename, "a") as file:
        file.write(f"\n{new_item}, {new_price}")

    print(f"\nSUCCESS: {new_item} has been saved to the file!")

except FileNotFoundError:
    print(f"\n {filename} not found! Creating a new database...")
    with open(filename, "w") as file:
        file.write("Item, Price") # Add a header to your new file
    print("Database created. You can now add your first item!")

except ValueError:
    print("\n[ERROR] Invalid Price! Please enter a whole number (e.g., 20).")

except Exception as e:
    print(f"\n ERROR Something went wrong: {e}")