"""CSC148 Lab 5: Linked Lists

=== CSC148 Fall 2020 ===
Department of Mathematical and Computational Sciences,
University of Toronto Mississauga

=== Module description ===

This module runs timing experiments to determine how the time taken
to call `len` on a Python list vs. a LinkedList grows as the list size grows.
"""
from timeit import timeit
from linked_list import LinkedList
from goated_list import GoatedList

NUM_TRIALS = 3000                        # The number of trials to run.
SIZES = [1000, 2000, 4000, 8000, 16000]  # The list sizes to try.


def profile_len(list_class: type, size: int) -> float:
    """Return the time taken to call len on a list of the given class and size.

    Precondition: list_class is either list or LinkedList.
    """
    # Create an instance of list_class containing <size> 0's.
    my_list = [0] * size

    # If it is a LinkedList
    if list_class == LinkedList:
        my_list = LinkedList(my_list)

    # If it is a GoatedList
    elif list_class == GoatedList:
        my_list = GoatedList(my_list)

    # call timeit appropriately to check the runtime of len on the list.
    # Look at the Lab 4 starter code if you don't remember how to use timeit:
    # https://mcs.utm.utoronto.ca/~148/labs/w4_ADTs/starter-code/timequeue.py
    return timeit('len(my_list)', number=1000, globals=locals())


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    # Try both Python's list and our LinkedList
    all_times = {}
    for list_class in [list, LinkedList, GoatedList]:
        times = []
        plt.figure()
        # Try each list size
        for s in SIZES:
            time = profile_len(list_class, s)
            times.append(time)
            print(f'[{list_class.__name__}] Size {s:>6}: {time}')
        # Plot the stuff
        plt.plot(SIZES, times)
        plt.xlabel('Sizes of the Lists')
        plt.ylabel('Time')
        plt.suptitle(f'{list_class.__name__}')
        plt.show()
