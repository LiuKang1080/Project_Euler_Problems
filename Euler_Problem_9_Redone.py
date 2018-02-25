# Script Name       : Euler_Problem_9_Redone.py
# Author            : Andrew Reddish, Shivakumar Mahakali
#
# Description       : Solution to Problem 9 from Project Euler.
#
# Problem 9         : A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#                     a^2 + b^2 = c^2 For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#                     There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#                     Find the product abc.


def pythagorean_triplet():
    """
    Calculate the Pythagorean Triplet.
    :return: [int] Product of the Pythagorean Triplet.
    """
    for c in range(3, 1000):
        c_sq = c**2
        for b in range(2, c - 1):
            a = 1000 - b - c
            if ((a**2) + (b**2)) == c_sq:
                return a * b * c


# Solution for the specific case of Euler problem number 9.
print(pythagorean_triplet())
