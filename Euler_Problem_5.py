# Script Name       : Euler_Problem_5.py
# Author            : Shivakumar Mahakali
#
# Description       : Solution to Problem 5 from Project Euler.
#
# Problem 1         : 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without
#                     any remainder. What is the smallest positive number that is evenly divisible by all of the
#                     numbers from 1 to 20?


def smallest_number(limit):
    """
    calculates the smallest number that can be evenly divisible by all numbers from 1 to limit.
    :param limit: Upper limit.
    :return: [int] Smallest number that is divisible by all numbers to limit.
    """
    # Populate empty list with number from 1 to limit.
    number_list = []
    for i in range(1, limit + 1):
        number_list.append(i)

    solution = []
    for number in range(limit, 999999999, limit):
        if all(number % num == 0 for num in number_list):
            solution.append(number)

        # Break out of the loop when we get the first index. Since the first index is the minimum, this is our solution.
        try:
            if solution[0] is not None:
                break
        except IndexError:
            continue

    return min(solution)


print(smallest_number(20))
