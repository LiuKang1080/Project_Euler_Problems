# Script Name       : Euler_Problem_7.py
# Author            : Shivakumar Mahakali
#
# Description       : Solution to Problem 7 from Project Euler.
#
# Problem 7         : By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime
#                     is 13. What is the 10,001st prime number?


def prime_check(num):
    """
    Checks to see if the provided number is a prime.
    :param num:
    :return: True / False
    """
    count = 0
    for i in range(2, num):
        # if checks to see if i and num are completely divisible if they are, they are not prime, break.
        if num % i == 0:
            return False
            break
        else:
            count += 1

    # we do num - 2 check because our loop starts at 2 not 0.
    if count == num - 2:
        return True


def prime_num_term(num):
    n = 0
    count = 0
    while count != num:
        n += 1
        if prime_check(n):
            # Count check is the index, if prime then add + 1 to index. Loop until count = provided number index.
            count += 1

    return n


# Solution for the specific case of Euler problem number 7.
print(prime_num_term(10001))
