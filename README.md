# Finding-primes
A quick way to find all the prime numbers in a given range

This code combines several techniques to find the prime numbers. These are as follows:

  Every composite number has a prime factor less than or equal to its square root. That is, given a number N, if we do not find a prime factor p[2 <= p <= sqrt(N)], it implies N             is a prime number. Source: https://proofwiki.org/wiki/Composite_Number_has_Prime_Factor_not_Greater_Than_its_Square_Root

  Every prime number[except for 2 and 3] can be written in the form of (6n - 1) or (6n + 1), where n is any natural number. I did not find any proof for this, but this holds true for the numbers between 1 to 1,000,000. Note: Not all numbers that satisfy 6n-1 or 6n+1 are prime numbers.

The flow of code is as follows:

Enter the number of test cases:T
Enter the min and max range separated by space. Make sure Max >= Min, and Min >= 0, otherwise, code would exit.

All test case ranges are separated by a newline character, while each prime is printed on a new line

This code takes roughly 6 seconds to find primes between 1 and 1,000,000.
