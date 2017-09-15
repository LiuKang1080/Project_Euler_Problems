# Script Name       : Euler_Problem_4.py
# Author            : Shivakumar Mahakali
#
# Description       : Solution to Problem 4 from Project Euler.
#
# Problem 4         : A palindromic number reads the same both ways. The largest palindrome made
#                     from the product of two 2-digit numbers is 9009 = 91 × 99.
#                     Find the largest palindrome made from the product of two 3-digit numbers.


my_list = []
for a in range(1, 1000):
    for b in range(1, 1000):
        num = a * b
        num_string = str(num)
        num_reverse = num_string[::-1]
        if num_string == num_reverse:
            my_list.append(num)

print(max(my_list))

#                   : Generic function to find the largest palindrome made from the product of number up to limit n.


def palindrome(limit):
    """
    Find the largest palindrome from the multiplication of all numbers to limit.
    :param limit: Upper limit.
    :return: [int] Maximum value from a list of palindromes.
    """
    num_list = []

    for x in range(1, limit):
        for y in range(1, limit):
            number = x * y
            number_string = str(number)
            number_reverse = number_string[::-1]

            if number_string == number_reverse:
                num_list.append(number)

    return max(num_list)
