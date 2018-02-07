"""
---*** THE PROBLEM ***---
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

---*** SOLUTION NOTES ***---
None, the problem is pretty self explanatory
"""


def sum_digits(number):
    # 'number' is the number whose digits will be summed.
    # Returns the sum of the digits of 'number'.

    #  Cast the number as a string.
    num_string = str(number)
    addition = 0

    # Iterate over the whole string.
    for i in range(0, len(num_string)):

        # Sum the elements together.
        addition += int(num_string[i])

    return addition

# Set program up for the initial conditions specified by the problem.
number = 2**1000

# Find the sum of the digits of the number.
solution = sum_digits(number)

# Print the solution
print(solution)
