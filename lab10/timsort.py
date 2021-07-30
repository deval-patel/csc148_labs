"""CSC148 Lab 10: More on sorting

=== CSC148 Winter 2021 ===
Department of Mathematical and Computational Sciences,
University of Toronto Mississauga

=== Module description ===
This file contains a mutating implementation of mergesort,
and a skeleton implementation of Timsort that you will work through
during this lab.
"""
from typing import Optional, List, Tuple


###############################################################################
# Introduction: mutating version of mergesort
###############################################################################
def mergesort2(lst: list,
               start: int = 0,
               end: Optional[int] = None) -> None:
    """Sort the items in lst[start:end] in non-decreasing order.

    Note: this is a *mutating, in-place* version of mergesort,
    meaning it does not return a new list, but instead sorts the input list.

    When we divide the list into halves, we don't create new lists for each
    half; instead, we simulate this by passing additional parameters (start
    and end) to represent the part of the list we're currently recursing on.
    """
    if end is None:
        end = len(lst)

    if start < end - 1:
        mid = (start + end) // 2
        mergesort2(lst, start, mid)
        mergesort2(lst, mid, end)
        _merge(lst, start, mid, end)


def _merge(lst: list, start: int, mid: int, end: int) -> None:
    """Sort the items in lst[start:end] in non-decreasing order.

    Precondition: lst[start:mid] and lst[mid:end] are sorted.

    >>> lst = [1, 4, 7, 10, 2, 5]
    >>> _merge(lst, 0, 4, 6)
    >>> lst
    [1, 2, 4, 5, 7, 10]
    """
    result = []
    left = start
    right = mid
    while left < mid and right < end:
        if lst[left] < lst[right]:
            result.append(lst[left])
            left += 1
        else:
            result.append(lst[right])
            right += 1

    # This replaces lst[start:end] with the correct sorted version.
    lst[start:end] = result + lst[left:mid] + lst[right:end]


###############################################################################
# Task 1: Finding runs
###############################################################################
def find_runs(lst: list) -> List[Tuple[int, int]]:
    """Return a list of tuples indexing the runs of lst.

    Precondition: lst is non-empty.

    >>> find_runs([1, 4, 7, 10, 2, 5, 3, -1])
    [(0, 4), (4, 6), (6, 7), (7, 8)]
    >>> find_runs([0, 1, 2, 3, 4, 5])
    [(0, 6)]
    >>> find_runs([10, 4, -2, 1])
    [(0, 1), (1, 2), (2, 4)]
    """
    runs = []

    # Keep track of the start and end points of a run.
    run_start = 0
    run_end = 1
    while run_end < len(lst):
        # How can you tell if a run should continue?
        #   (When you do, update run_end.)

        # intial: lst[1] > lst[0]
        # if lst[run_end] > lst[run_end -1]:
        #     run_end += 1
        # else:
        #     runs.append((run_start,run_end))
        #     run_start = run_end
        #     run_end += 1

        # How can you tell if a run is over?
        #   (When you do, update runs, run_start, and run_end.)

        if lst[run_end] < lst[run_end - 1]:
            runs.append((run_start, run_end))
            run_start = run_end
        run_end  += 1

    runs.append((run_start, run_end))
    return runs


###############################################################################
# Task 2: Merging runs
###############################################################################
def timsort(lst: list) -> None:
    """Sort <lst> in place.

    >>> lst = []
    >>> timsort(lst)
    >>> lst
    []
    >>> lst = [1]
    >>> timsort(lst)
    >>> lst
    [1]
    >>> lst = [1, 4, 7, 10, 2, 5, 3, -1]
    >>> timsort(lst)
    >>> lst
    [-1, 1, 2, 3, 4, 5, 7, 10]
    """
    runs = find_runs(lst)
    # [1, 4, 7, 10, 2, 5, 3, -1]            <- lst
    # [(0, 4), (4, 6), (6, 7), (7, 8)]      <- runs
    # _merge(lst, starting, midpoint, end)
    
    # while <runs> has more than one tuple:
    #     pop the top two runs off the stack <runs>
    #     merge the runs in <lst>, which produces a new run
    #     push the new run onto <runs>
    
    mid_end = (0,len(lst))
    while len(runs) > 1:
        mid_end = runs.pop()
        start_mid = runs.pop()
        # merge(lst, 6, 7,8)    1st run
        # merge(lst,0 ,4, 6)    2nd run
        # lst[0:6] is sorted
        # lst[6:8] is sorted.
        _merge(lst, start_mid[0],start_mid[1], mid_end[1])

    # merge(lst, 0, 6, 8)
    _merge(lst, 0, mid_end[1], len(lst))

    # Treat runs as a stack and repeatedly merge the top two runs
    # When the loop ends, the only run should be the whole list.
    # HINT: you should be able to use the "_merge" function provided
    # in this file.

    # This would work but wastes a lot of resources
    # i = 0
    # while i < len(runs) - 1:
    #     _merge(lst, 0, runs[i][1], runs[i+1][1])  
    #     i += 1


###############################################################################
# Task 3: Descending runs
###############################################################################
def find_runs2(lst: list) -> List[Tuple[int, int]]:
    """Return a list of tuples indexing the runs of lst.

    Now, a run can be either ascending or descending!

    Precondition: lst is non-empty.

    First set of doctests, just for finding descending runs.
    >>> find_runs2([5, 4, 3, 2, 1])
    [(0, 5)]
    >>> find_runs2([1, 4, 7, 10, 2, 5, 3, -1])
    [(0, 4), (4, 6), (6, 8)]
    >>> find_runs2([0, 1, 2, 3, 4, 5])
    [(0, 6)]
    >>> find_runs2([10, 4, -2, 1])
    [(0, 3), (3, 4)]

    The second set of doctests, to check that descending runs are reversed.
    >>> lst1 = [5, 4, 3, 2, 1]
    >>> find_runs2(lst1)
    [(0, 5)]
    >>> lst1  # The entire run is reversed
    [1, 2, 3, 4, 5]
    >>> lst2 = [1, 4, 7, 10, 2, 5, 3, -1]
    >>> find_runs2(lst2)
    [(0, 4), (4, 6), (6, 8)]
    >>> lst2  # The -1 and 3 are switched
    [1, 4, 7, 10, 2, 5, -1, 3]
    """
    # Hint: this is very similar to find_runs, except
    # you'll need to keep track of whether the "current run"
    # is ascending or descending.

    # [1, 4, 7, 10, 2, 5, 3, -1]
    # How do we know if it's ascending or decending?
    # Compare subsequent items in the list
    # 
    
    # while the not at the end of the list
    # if it is STILL increasing or decreasing
    # continue
    # else
    # stop, append run
    
    runs = []

    # Keep track of the start and end points of a run.
    run_start = 0
    run_end = 1
    current_run = None  # Represents ascending

    while run_end < len(lst):
        # if the next index is ascending
        if lst[run_end] > lst[run_end -1]:
            # if it's already descending
            if current_run == False:
                runs.append((run_start,run_end))
                mergesort2(lst, run_start,run_end)
                run_start = run_end
                current_run = None
            # if it's just ascending
            else:
                current_run = True

        # if the next index is descending
        elif lst[run_end] < lst[run_end -1]:
            # if it was already ascending
            if current_run:
                runs.append((run_start,run_end))
                run_start = run_end
                current_run = None
            # if it's just descending
            else:
                current_run = False
        
        run_end += 1
    if run_start != run_end:
        runs.append((run_start, run_end))
        mergesort2(lst, run_start,run_end)

    return runs

    # Alternative Solution
    # runs = []
    # # Keep track of the start and end points of a run.
    # run_start = 0
    # run_end = 1

    # status = str(lst[1] - lst[0])

    # while run_end < len(lst):
    #     if ('-' in str(lst[run_end] - lst[run_end - 1]) and '-' not in status) or \
    #         ('-' not in str(lst[run_end] - lst[run_end - 1]) and '-' in status):
    #         if '-' not in str(lst[run_end] - lst[run_end - 1]) and '-' in status:
    #             mergesort2(lst, run_start, run_end)
    #         runs.append((run_start, run_end))
    #         run_start = run_end
    #         if run_end + 1 < len(lst):
    #             status = str(lst[run_end + 1] - lst[run_end])
    #     run_end  += 1
        
    # if run_start != run_end:
    #     runs.append((run_start, run_end))
    #     mergesort2(lst, run_start, run_end)

    # return runs

###############################################################################
# Task 4: Minimum run length
###############################################################################
MIN_RUN = 64


def find_runs3(lst: list) -> List[Tuple[int, int]]:
    """Same as find_runs2, but each run (except the last one)
    must be of length >= MIN_RUN.

    Precondition: lst is non-empty
    """

    # In the loop, after it has found an ascending or descending run (but before reversing the descending run), 
    # if the run has length less than 64, sort it and the next few elements after it using insertion sort, 
    # to create an ascending run of length 64. Then add that run to the stack.

    runs = []

    # Keep track of the start and end points of a run.
    run_start = 0
    run_end = 1
    current_run = None  # Represents ascending

    while run_end < len(lst):
        # if the next index is ascending
        if lst[run_end] > lst[run_end -1]:
            # if it's already descending
            if current_run == False:
                enough = run_end - run_start
                if enough < MIN_RUN:
                    run_end += enough
                    insertion_sort(lst, run_start, run_end)
                runs.append((run_start,run_end))

                run_start = run_end
                current_run = None
            # if it's just ascending
            else:
                current_run = True

        # if the next index is descending
        elif lst[run_end] < lst[run_end -1]:
            # if it was already ascending
            if current_run:
                enough = run_end - run_start
                if enough < MIN_RUN:
                    run_end += enough
                    insertion_sort(lst, run_start, run_end)
                runs.append((run_start,run_end))
                run_start = run_end
                current_run = None
            # if it's just descending
            else:
                current_run = False
        
        run_end += 1
    if run_start != run_end:
        runs.append((run_start, run_end))
        mergesort2(lst, run_start,run_end)

    return runs


def insertion_sort(lst: list, start: int, end: int) -> None:
    """Sort the items in lst[start:end] in non-decreasing order.
    """
    for i in range(start + 1, end):
        num = lst[i]
        left = start
        right = i
        while right - left > 1:
            mid = (left + right) // 2
            if num < lst[mid]:
                right = mid
            else:
                left = mid + 1

        # insert
        if lst[left] > num:
            lst[left + 1:i + 1] = lst[left:i]
            lst[left] = num
        else:
            lst[right+1:i+1] = lst[right:i]
            lst[right] = num


###############################################################################
# Task 5: Optimizing merge
###############################################################################
def _merge2(lst: list, start: int, mid: int, end: int) -> None:
    """Sort the items in lst[start:end] in non-decreasing order.

    Precondition: lst[start:mid] and lst[mid:end] are sorted.
    >>> lst = [1, 4, 7, 10, 2, 5]
    >>> _merge2(lst, 0, 4, 6)
    >>> lst
    [1, 2, 4, 5, 7, 10]
    """

    # The provided _merge algorithm creates a new list that reaches the same size as the original list, and 
    # then copies the contents back over to the original.

    # Let’s optimize that a little bit by making the following observation: 
    # suppose we want to merge two consecutive runs A and B in the list. 
    # We can copy A to a temporary storage, and then just start filling in entries where A used to be 
    # (running the standard merge algorithm on B and the copy of A).

    # This works because the number of “unused” spaces in the list is equal to the number of entries of A 
    # still remaining in the temporary storage.

    temp_list = lst[start:mid]
    left = start
    right = mid

    # lst = [1, 4, 7, 10, 2, 5]
    #       [1, 2, 7, 10, 4, 5]
    # temp_list = [1, 4, 7, 10]
    # right_list = [2, 5]
    # left list and right list needs to be sorted at all times
    
    while left< mid  and right < end:
        if lst[left] > lst[right]:
            lst[left] = lst[right]
            lst[right] = temp_list[left]
            if lst[left + 1] < lst[right]:
                right += 1
        
        left += 1
        print(lst)
###############################################################################
# Task 6: Limiting the 'runs' stack
###############################################################################
def timsort2(lst: list) -> None:
    """Sort the given list using the version of timsort from Task 6.
    """
    pass


if __name__ == '__main__':
    import doctest
    doctest.testmod()