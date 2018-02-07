"""
---*** THE PROBLEM ***---
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

---*** SOLUTION NOTES ***---
Although projecteuler.net recommends using a computer for this problem it was not necessary.
The smallest number that is divisible by every number in a given range can be found by multiplying all the highest order
prime factorisations in that range.

For example in the range 1 to 10:
1*2*3*4*5*6*7*8*9*10 is a solution the problem, but it is not the smallest possible solution.
To reduce the size of the answer we can remove the 2, the 3, the 4, the 6, and the 10. Since their prime factors
already show up in larger numbers of the product.
This leaves us with 1*5*7*8*9 = 2520
Reduced to prime factors this leaves 5*7*(2*2*2)*(3*3)

Then for the question in the range 1 to 20:
1*2*3*...*19*20 can be reduced by removing all numbers apart from 1, 5, 7, 9, 11, 13, 16, 17, and 19.
1*5**7*9*11*13*16*17*19 = 232792560, the correct solution.
(Reduced to prime factors this leaves 5*7*(3*3)*11*13*(2*2*2*2)*17*19)
Each prime factor is included the maximum amount of times it appears in any of numbers.
"""
