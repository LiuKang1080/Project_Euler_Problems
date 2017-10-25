# Script Name       : Euler_Problem_7.py
# Author            : Shivakumar Mahakali
#
# Description       : Solution to Problem 7 from Project Euler.
#
# Problem 7         : By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime
#                     is 13. What is the 10,001st prime number?


def prime_check(num):
    count = 0
    for i in range(2, num):
        if num % i == 0:
            return False
            break
        else:
            count += 1

    if count == num - 2:
        return True


def prime_num_term(num):

