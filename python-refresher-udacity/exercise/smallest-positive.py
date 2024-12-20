def smallest_positive(in_list):
    # TODO: Define a control structure that finds the smallest positive
    # number in in_list and returns the correct smallest number.
    smallest_positive = None

    for num in in_list:
        if num > 0:
            if smallest_positive is None or num < smallest_positive:
                smallest_positive = num
                
    return smallest_positive

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2
