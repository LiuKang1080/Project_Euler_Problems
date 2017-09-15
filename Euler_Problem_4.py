# Script Name       : Euler_Problem_4.py
# Author            : Shivakumar Mahakali
#
# Description       : Solution to Problem 4 from Project Euler.
#
# Problem 4         : A palindromic number reads the same both ways. The largest palindrome made
#                     from the product of two 2-digit numbers is 9009 = 91 × 99.
#                     Find the largest palindrome made from the product of two 3-digit numbers.


def palindrome(limit):
    """
    Find the largest palindrome from the multiplication of all numbers up to the limit.
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


# Solution for the specific case of Euler problem number 4.
solution = palindrome(1000)
print(solution)
