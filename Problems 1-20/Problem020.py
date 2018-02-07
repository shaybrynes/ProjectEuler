"""
---*** THE PROBLEM ***---
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

---*** SOLUTION NOTES ***---
The problem is self explanatory, string manipulation required.
"""


def factorial(n):
    # 'n' is the number whose factorial will be found, and then its digits will be summed.
    # Returns the factorial of 'n'.

    fact = 1

    # Iterate over the all the terms to find the factorial.
    for i in range(1, n):

        fact *= i

    return fact


def sum_digits(number):
    # 'number' is an integer that will have its digits summed.

    # Cast the number as a string.
    num_string = str(factorial(number))
    summation = 0

    # Iterate over all the digits in the number.
    for i in range(0, len(num_string)):

        # Sum the digits.
        summation += int(num_string[i])

    return summation


# Set program up for the initial conditions specified by the problem.
number = 100

# Find the sum of the digist in the factorial on 'number'.
solution = sum_digits(number)

# Print the solution.
print(solution)
