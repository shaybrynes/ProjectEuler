"""
---*** THE PROBLEM ***---
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

---*** SOLUTION NOTES ***---
The simplest way to solve this is to iterate over 'a' and 'b', by iterating over 'a', and increasing 'b' when 'a'
becomes greater than 'b'.
"""


def find_c(a, b):
    # 'a' and 'b' are the values on the left hand side of the potential Pythagorean triple.
    # Returns the value of 'c' for the potential Pythagorean triple.

    c = ((a**2) + (b**2))**0.5

    return c


def pythagorean_triples(expectant):
    # expectant is the sum of 'a', 'b' and 'c' of the Pythagorean Triple to find.
    # Returns the Pythagorean triple, '[a, b, c]'.

    a, b = [3, 3]

    while True:

        # Since 'a < b' increase 'b' and reset 'a' when 'a' becomes equal to 'b'.
        if a == b:
            b += 1
            a = 1

        # Find the value of c that 'a' and 'b' produce.
        c = find_c(a, b)

        # If these values sum to the expectant value they should be returned.
        if a + b + c == expectant:
            break

        if b > expectant:
            return False

        # Add to the iterative value of 'a'.
        a += 1

    return [a, b, c]


def product_pythag_triples(expectant):
    # expectant is the sum of 'a', 'b' and 'c' of the Pythagorean Triple to find.
    # Returns the product of the Pythagorean triple, '[a, b, c]'.

    triple = pythagorean_triples(expectant)
    product = 1

    # Iterate over the returned triple.
    for i in range(0, len(triple)):

        # Calculate the product of the terms in the triple.
        product *= triple[i]

    return product


# Set program up for the initial conditions specified by the problem.
expectant = 1000

# Find the product of the pythagorean triple.
product = product_pythag_triples(expectant)

# Print the product.
print(product)
