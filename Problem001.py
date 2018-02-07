"""
---*** THE PROBLEM ***---
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

---*** SOLUTION NOTES ***---
The 'i'th term of a iteration is divisible by 'n' if 'i' mod 'n' is 0.
!Numbers divisible by 3 and 5 should only be counted once! (3 or 5 as specified).
"""


def divisible_by(n, i):
    # 'i' is the dividend, 'n' is divisor.
    # Returns True if remainder of 'i'/'n' is 0.

    if i % n == 0:
        return True

    else:
        return False


def sum_of_multiples(bound, divisors):
    # 'bound' is the range to sum between, divisors is the list of multiples to check for.
    # Returns the sum of the multiples.

    addition = 0

    # Iterate of the range specified, in a step of one.
    for i in range(bound[0], bound[1], 1):

        # Iterate over all of the divisors specified.
        for j in range(0, len(divisors)):

            # If the iterator is divisible by the divisor, add to the final sum.
            if divisible_by(divisors[j], i):
                addition += i

                # Terms divisible by 3 and 5 (15 for example) should only be counted once.
                # Hence break the inner loop to prevent those numbers being recounted.
                break

    return addition


# Set program up for the initial conditions specified by the problem.
bound = [0, 1000]
divisors = [3, 5]

# Find the sum of the multiples.
solution = sum_of_multiples(bound, divisors)

# Print the solution.
print(solution)



