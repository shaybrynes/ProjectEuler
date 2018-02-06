"""
---*** THE PROBLEM ***---
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

---*** SOLUTION NOTES ***---
Produce a list of all 6 digit palindromic numbers,
then create a list of the products of all 3 digit numbers that produce a palindromic number.
sort and select the largest.
"""


def generate_palin_list(num_of_digits):
    # 'num_of_digits' is the number of digits the product elements of the palindromic number are made of.
    # Returns a list of all the palindromic numbers below 2*num_of_digits

    palindromic_list = []

    # Iterate over all the numbers with 'num_of_digits'
    for i in range(10**(num_of_digits - 1), 10**num_of_digits):

        # Cast the number as a string and add a flipped version to create a palindromic number, cast that as an integer.
        palindromic_num = int(str(i) + str(i)[::-1])

        # Append it to a list of palindromic numbers
        palindromic_list.append(palindromic_num)

    return palindromic_list


def find_palin_numbers(num_of_digits):
    # 'num_of_digits' is the number of digits the product elements of the palindromic number are made of.
    # Returns a list of all the palindromic products made of 2*num_of_digits

    palindromic_list = generate_palin_list(num_of_digits)
    solutions = []

    # Iterate over all the numbers with 'num_of_digits' from largest to smallest
    for i in range(10**num_of_digits, 10**(num_of_digits - 1), -1):

        # Iterate over this region again, but reduce the size of this region over all iterations,
        # prevents double calculations of products
        for j in range(i, 10**(num_of_digits - 1), -1):

                # If the product of the two iterations is palindromic then add it to a solutions list
                if i*j in palindromic_list:
                    solutions.append(i*j)

    return solutions


# Set program up for the initial conditions specified by the problem.
number_of_digits = 3

# Find all the palindromic products for this number of digits
palindromic_products = find_palin_numbers(number_of_digits)

# Print the largest palindromic solution
print(max(palindromic_products))

