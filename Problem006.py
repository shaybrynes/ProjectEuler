"""
---*** THE PROBLEM ***---
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

---*** SOLUTION NOTES ***---
None, the problem is very self explanatory.
"""


def sum_of_squares(upper):
    # 'upper' is the maximum square to include in the sum.
    # Returns the sum of the squares of the integers in the range

    addition = 0

    # Iterate over all the values in the range
    for i in range(0, upper + 1):

        # Add the square of the next value.
        addition += i**2

    return addition


def square_of_sum(upper):
    # 'upper' is the maximum square to include in the sum.
    # Returns the square of the sum of the integers in the range

    addition = 0

    # Iterate over all the values in the range
    for i in range(0, upper + 1):
        # Add the next value to the previous ones.
        addition += i

    # Square the sum
    addition = addition**2

    return addition

# Set program up for the initial conditions specified by the problem.
upper = 100

# Find the difference between the square of the sum and the sum of the squares
difference = square_of_sum(upper) - sum_of_squares(upper)

# Print the difference
print(difference)
