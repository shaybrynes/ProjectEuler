"""
---*** THE PROBLEM ***---
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

---*** SOLUTION NOTES ***---
Used the prime generator used in problem 7 with little modifications.
"""

from math import floor


def generate_primes(upper):
    # 'upper' is the upper bound for the maximum term of the primes, does not create this term.
    # Returns a list of prime numbers

    # Start with a list of the first primes to kick start the program.
    primes = [2, 3, 5]

    # Find primes over the range between the next prime, 7, and the upper bound. Increase efficiency by not testing even
    # numbers (2 is the only even prime).
    for i in range(7, upper, 2):

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

    return primes


def sum_of_primes(primes):
    # 'primes' is a list of the prime numbers found.

    addition = 0

    # Iterate of the list of the prime numbers.
    for i in range(0, len(primes)):

        # Sum them together.
        addition += primes[i]

    return addition


# Set program up for the initial conditions specified by the problem.
upper = 2000000

# Find the primes below limit
prime_numbers = generate_primes(upper)

# Sum these primes
solution = sum_of_primes(prime_numbers)

# Print the solution
print(solution)
