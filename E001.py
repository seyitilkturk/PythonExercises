"""
Given a list, write a Python program to swap first and last element of the list.

Input : [12, 35, 9, 56, 24]
Output : [24, 35, 9, 56, 12]

"""


def swap(given_list):
    len_list = len(given_list)
    temp = given_list[0]
    given_list[0] = given_list[len_list-1]
    given_list[len_list-1] = temp

    return given_list


print(swap([1, 2, 3, 4, 5, 6]))




