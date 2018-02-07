"""
---*** THE PROBLEM ***---
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved
yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

---*** SOLUTION NOTES ***---

"""


def compare_largest(largest, competitor):
    # 'largest' is the current largest length of the Collatz chain, 'competitor' is the value that could be the largest.
    # Returns the new, or old value of the largest length of the Collatz chain.

    if largest[1] > competitor[1]:
        return largest

    else:
        return competitor


def find_length_collatz(starting_number):
    # 'starting_number' is the first number of the Collatz chain.
    # Returns a list of [starting_number, length] of the Collatz chain

    chain = starting_number
    length = 1

    # Iterate whilst the number in the chain is not 1.
    while True:

        # If the chain number is even.
        if chain % 2 == 0:
            # The next number is half the current one.
            chain = (chain / 2)
            length += 1

        else:
            # The next number is 3 times the number plus one.
            chain = (3 * chain) + 1
            length += 1

        if chain == 1:
            break

    return [starting_number, length]


def largest_collatz(maximum_start):
    # 'maximum_start' is the largest starting number that will be tested.
    # Returns the a list of [starting_number, length] of the largest Collatz chain.

    starting_number = 2
    current_largest = [1, 1]

    while starting_number < maximum_start:
        # Find the length of the Collatz chain.
        competitor = find_length_collatz(starting_number)

        # See if this value is longer than the current longest.
        current_largest = compare_largest(current_largest, competitor)

        starting_number += 1

    return current_largest


# Set program up for the initial conditions specified by the problem.
maximum_start = 1000000

# Find the longest Collatz chain below this value.
solution = largest_collatz(maximum_start)

# Print the solution.
print(solution[0])



