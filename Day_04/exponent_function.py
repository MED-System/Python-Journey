# Function to calculate power (e.g., 2 to the power of 3)
def raise_to_power(base_num, pow_num):
    # Start with 1 because multiplying by 0 would ruin the math
    result = 1

    # The loop runs exactly 'pow_num' times
    for index in range(pow_num):
        # Every time the loop runs, multiply the result by the base
        result = result * base_num
    return result


# Test the function: 2 * 2 * 2 = 8
print(raise_to_power(2, 3))