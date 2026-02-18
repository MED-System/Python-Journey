from library1 import Food
dish_name = input("Enter food name: ")
dish_price = input("Enter food price: ")
dish_details = Food(dish_name, dish_price)

file = open("menu.txt", "a")
file.write(dish_details.dish_name + " costs  " + dish_details.price + " dollars\n")
file.close()