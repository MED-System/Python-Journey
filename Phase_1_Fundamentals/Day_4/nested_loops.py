# A 2D List
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
# This first loop grabs one row at a time
for row in number_grid:
    # This second loop grabs every number inside that row
    for col in row:
        # This prints every number one by one until the list is empty
        print(col)