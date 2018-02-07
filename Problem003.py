"""
---*** THE PROBLEM ***---
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

---*** SOLUTION NOTES ***---
If the largest prime factor any number can have is the perfect 2nd root of that number,
hence generate a list of primes less than or equal to the square root of the number.
Then check these primes to see if they are factors of the number, the solution is the largest of these
"""

from math import floor


def is_factor_of(num, factor):
    # 'factor' is the divisor, 'num' is dividend.
    # Returns 0 if the divisor is a factor of the dividend.

    if num%factor == 0:
        return True

    else:
        return False


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


def find_prime_factors_of(num):
    # 'num' is the number to find prime factors of.
    # Returns a list of the prime factors of 'num'.

    # The primes up to the square root of the number are needed, so generate the list of these primes.
    primes = generate_primes(floor(num**0.5))
    prime_factors = []

    # Iterate over the list of primes to see if each is a factor of the number being tested
    for i in range(0, len(primes)):

        # Each prime factor may appear more than once. For example the prime factors of 20 are 2, 2, and 5.
        # Hence need to test the same number multiple times to make sure it is completely tested.
        while True:

            # If the prime is a factor of the number
            if is_factor_of(num, primes[i]):

                # Add the prime to the list of prime factors
                prime_factors.append(primes[i])

                # Divide the number by the prime factor
                num /= primes[i]

            # If the prime is not a factor, skip to the next prime.
            else:
                break

    return prime_factors


# Set program up for the initial conditions specified by the problem.
number = 600851475143

# Find the prime factors of the number.
prime_factors = find_prime_factors_of(number)

# Print the largest prime factor.
print(max(prime_factors))
