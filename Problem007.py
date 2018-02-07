"""
---*** THE PROBLEM ***---
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

---*** SOLUTION NOTES ***---
Used the prime generator used in problem 3 with a few modifications.
"""

from math import floor


def generate_primes(limit):
    # 'limit' is the number of primes to find.
    # Returns a list of prime numbers

    # Start with a list of the first primes to kick start the program.
    primes = [2, 3, 5]
    i = 7

    # Find primes over the range between the next prime, 7, and the limit. Increase efficiency by not testing even
    # numbers (2 is the only even prime).
    while True:

        # When testing the iterator 'i' for primality see if it divisible by other primes. If not then 'i' itself is
        # prime. Hence iterate over the list of primes already found to see if 'i' is divided perfectly by any elements.
        for number in primes:

            # If 'i' divides exactly it is not prime, end the test for 'i'.
            if i % number == 0:
                break

            # If i does not divide exactly with any of the element is the list, then it must be prime,
            # go on to the next iterator.
            # 'floor(i**0.5)' is the square root of i rounded down, this prevents over testing.
            elif number > floor(i**0.5):
                primes.append(i)
                break

        # If the number of primes has been found, then end the operation
        if len(primes) == limit:
            break

        # Increase the iterator
        i += 2

    return primes

# Set program up for the initial conditions specified by the problem.
limit = 10001

# Find the primes in this region
primes = generate_primes(limit)

# Print the last prime
print(primes[-1])
