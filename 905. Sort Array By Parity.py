"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.
"""


def sortArrayByParity(A: list):
    even = []
    odd = []
    for i in A:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print(even + odd)
    return (even + odd)


sortArrayByParity([3, 1, 2, 4])
