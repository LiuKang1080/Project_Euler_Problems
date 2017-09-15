# Script Name       : Euler_Problem_3.py
# Author            : Shivakumar Mahakali
#
# Description       : Solution to Problem 3 from Project Euler.
#
# Problem 3         : The prime factors of 13195 are 5, 7, 13 and 29.
#                     What is the largest prime factor of the number 600851475143 ?


def largest_prime(num):
    """
    Find largest prime factor of a given number.
    :param num: Number.
    :return: [int] maximum value within the list of prime numbers
    """
    i = 2
    prime_list = []

    while i*i <= num:
        # The largest prime number of (num) can NOT be greater than the square root of num.
        # (largest prime number)^2 <= num.

        while num > 1:
            # Num will break down by each prime divisor, this loop will continue until the divisor
            # cannot be broken down any further.

            while num % i == 0:
                # Append all prime numbers to list.

                prime_list.append(i)
                num = num / i
            i += 1

    print(max(prime_list))


largest_prime(600851475143)
