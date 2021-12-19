"""
Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.

Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
Output : [19, 65, 23, 90]

Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
Output : [1, 5, 3, 4, 2]

"""


def swap(given_list, pos1, pos2):
    temp = given_list[pos1]
    given_list[pos1] = given_list[pos2]
    given_list[pos2] = temp

    return given_list


print(swap([1, 2, 3, 4, 5, 6], 1, 2))
