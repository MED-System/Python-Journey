lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]

# Create a separate copy of the list to keep the original data safe
friends2 = friends.copy()
print(friends2)

# Flip the order of the friends list
friends.reverse()
print(friends)

# Sort numbers from smallest to largest
lucky_numbers.sort()
print(lucky_numbers)

# Add creed to the end of the list
friends.append("creed")

# Put kelly at index 1
friends.insert(1, "kelly")

print(friends)