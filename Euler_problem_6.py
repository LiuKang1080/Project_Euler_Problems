# Script Name       : Euler_Problem_6.py
# Author            : Shivakumar Mahakali
#
# Description       : Solution to Problem 6 from Project Euler.
#
# Problem 4         : The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
#                     The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025
#                     Hence the difference between the sum of the squares of the first ten natural numbers and the
#                     square of the sum is 3025 − 385 = 2640. Find the difference between the sum of the squares of
#                     the first one hundred natural numbers and the square of the sum.


def difference(limit):
    """
    Difference between the square of sums and the sum of squares of all numbers from 1 to the limit.
    :param limit: Upper limit of calculation.
    :return: [int] Absolute value of the difference.
    """
    sum_of_squares = []
    square_of_sums = []

    for num in range(1, limit + 1):
        sum_of_squares.append(num**2)
        square_of_sums.append(num)

    total_sum_of_squares = sum(sum_of_squares)

    total_square_of_sums = sum(square_of_sums)
    total_square_of_sums = (total_square_of_sums ** 2)

    return abs(total_square_of_sums - total_sum_of_squares)


print(difference(100))
