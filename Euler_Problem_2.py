# Script Name       : Euler_Problem_2.py
# Author            : Shivakumar Mahakali
#
# Description       : Solution to Problem 2 from Project Euler.
#
# Problem 2         : Each new term in the Fibonacci sequence is generated by adding the previous two terms.
#                     By starting with 1 and 2, the first 10 terms will be: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#                     By considering the terms in the Fibonacci sequence whose values do not exceed four million,
#                     find the sum of the even-valued terms.


def fibonacci(n):
    """
    Calculates the sum of all even numbered values in the fibonacci sequence.
    :param n: Value of the limit within the sequence.
    :return: [int] count
    """
    x, y = 0, 1
    count = 0
    for i in range(n):
        x, y = y, x + y

        if y % 2 == 0:
            count += y

        if y >= n:
            # When the term in the sequence reaches value n, return total sum of even numbers; return count.
            return count


# Solution for the specific case of Euler problem number 2.
solution = fibonacci(4000000)
print(solution)