def bigoh3(n: int) -> int:
    res = 0
    i = 0
    # Outer loop goes n^2 times
    # While i < n^2
    while i < n * n:
        # This is the only one which happens
        if i % 148 == 0:
            j = 1
            # O(n)
            while j < n:
                res = res + j  # This doesnt affect complexity, O(1)
                j = j + 18
            i += 148
    #    Never happens
        else:
            j = 1
            while j < n * n:
                res += j
                j = j * 7
            i += 7
    return res


# O(n^3)


"""

10:24 PM
    1  lst = [1, 2, 3] (1 or 4)

    2  lst = lst + [4, 5, 6] (2 or 5)

    3  lst2 = lst (0)

    4  lst2.append(lst[:]) (1)

# How many objects are created in pythion memory model?

"""


def find_width(lst, depth=0):
    # Base case, check if it is an int, return 0 length
    if isinstance(lst, int):
        return 0
    # This is a lst
    else:
        # Initialize the max width so far to be the length of this outer list
        max_width = 0

        # Go through all nested lists find the max width
        for sublist in lst:
            # Make a recursive call on each sublist, and get its max width.
            sublist_max_width = find_width(sublist, depth + 1)
            # If a sublist has a bigger width than the current length of the list.
            # Update it.
            if sublist_max_width > max_width:
                max_width = sublist_max_width

        # if outer layer, then return whatever found so far.
        if depth == 0:
            return max_width
        # If it is a nested list, the depth is not equial to 0, so compare it with current length
        # of the list.
        if len(lst) > max_width:
            max_width = len(lst)

        return max_width


def test_find_width():
    assert find_width([1, 2, 3]) == 0
    assert find_width([]) == 0
    assert find_width(4) == 0
    assert find_width([[1, 2, 3]]) == 3
    assert find_width([[1, 2, 3], 45, 57]) == 3
    assert find_width([[1, 2, 3], [1, 2, 3, 4]]) == 4


if __name__ == '__main__':
    import pytest
    pytest.main(['demo1.py'])
