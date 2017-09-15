# Script Name       : Euler_Problem_1.py
# Author            : Shivakumar Mahakali
#
# Description       : Solution to Problem 1 from Project Euler.
#
# Problem 1         : If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#                     The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.


total_count = 0
for num in range(0, 1000):
    if num % 3 == 0 or num % 5 == 0:
        total_count += num

print(total_count)


#                   : Generic function to find the sum of all multiples of 3 or 5 below number n.


def multiple(limit):
    """
    Find sum of all numbers below the limit number that are multiples of 3 and 5.
    :param limit: Upper limit number.
    :return: [int] total_sum
    """

    total_sum = 0
    for number in range(1, limit):
        if number % 3 == 0 or number % 5 == 0:
            total_sum += number

    return total_sum
