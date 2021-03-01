"""
Pure Python implementation of the jump search algorithm.
This algorithm iterates through a sorted collection with a step of n^(1/2),
until the element compared is bigger than the one searched.
It will then perform a linear search until it matches the wanted number.
If not found, it returns -1.
"""

import math


def jump_search(arr: list, x: int) -> int:
    """
    Pure Python implementation of the jump search algorithm.
    Examples:
    >>> jump_search([0, 1, 2, 3, 4, 5], 3)
    3
    >>> jump_search([-5, -2, -1], -1)
    2
    >>> jump_search([0, 5, 10, 20], 8)
    -1
    >>> jump_search([0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610], 55)
    10
    """

    """edge cases"""
    if len(arr) == 0:
        return -1
    if arr[0] > x:
        return -1
    if arr[len(arr) - 1] < x:
        return -1

    targetIndex = -1
    length = len(arr) - 1
    lowerBound = 0
    upperBound = arr[length]
    block = math.floor(math.sqrt(x))

    for index in range(0, length, block):
        if arr[index] < x:
            lowerBound = index
        else:
            upperBound = index
            break

    for index in range(lowerBound, upperBound, 1):
        if arr[index] == x:
            targetIndex = index
            break

    return targetIndex


if __name__ == "__main__":
    user_input = input("Enter numbers separated by a comma:\n").strip()
    arr = [int(item) for item in user_input.split(",")]
    x = int(input("Enter the number to be searched:\n"))
    res = jump_search(arr, x)
    if res == -1:
        print("Number not found!")
    else:
        print(f"Number {x} is at index {res}")
