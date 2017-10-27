# Script Name       : Euler_Problem_9.py
# Author            : Shivakumar Mahakali
#
# Description       : Solution to Problem 9 from Project Euler.
#
# Problem 9         : A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#                     a^2 + b^2 = c^2 For example, 32 + 42 = 9 + 16 = 25 = 52.
#                     There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#                     Find the product abc.


def pythagorean_triplet():
    """
    Calculate the Pythagorean Triplet.
    :return: [int] Product of the Pythagorean Triplet.
    """
    triplet_list = []

    for c in range(1, 1000):
        for b in range(1, 1000):
            for a in range(1, 1000):
                if (a + b + c) == 1000 and ((a**2) + (b**2)) == (c**2) and a < b < c:
                    triplet_list.append(a * b * c)

        try:
            if triplet_list[0] is not None:
                break
        except IndexError:
            continue

    return triplet_list[0]


# Solution for the specific case of Euler problem number 9.
print(pythagorean_triplet())
