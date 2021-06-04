"""Lab 5: Linked List Exercises

=== CSC148 Fall 2020 ===
Department of Mathematical and Computational Sciences,
University of Toronto Mississauga

=== Module Description ===
This module contains the code for a linked list implementation with two classes,
GoatedList and _Node.

All of the code from lecture is here, as well as some exercises to work on.
"""
from __future__ import annotations
from typing import Any, List, Optional, Union


class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the GoatedList class, but not by client code.

    === Attributes ===
    item:
        The data stored in this node.
    next:
        The next node in the list, or None if there are no more nodes.
    """
    item: Any
    next: Optional[_Node]

    def __init__(self, item: Any) -> None:
        """Initialize a new node storing <item>, with no next node.
        """
        self.item = item
        self.next = None  # Initially pointing to nothing


class GoatedList:
    """A linked list implementation of the List ADT.
    """
    # === Private Attributes ===
    # _first:
    #     The first node in the linked list, or None if the list is empty.
    #
    # _length:
    #     The number of nodes in this linked list.
    #
    # === Representation Invariant ===
    # _length:
    #     Is a non-negative number and represents the number of nodes in our linked list.

    _first: Optional[_Node]
    _length: int

    def __init__(self, items: list) -> None:
        """Initialize a new linked list containing the given items.

        The first node in the linked list contains the first item
        in <items>.
        """
        self._first = None
        # Add default length
        self._length = 0
        # Have a loop tracking variable
        curr = None
        # Iterate through the items list.
        for item in items:
            # Create a node containing this item
            node = _Node(item)
            # Add this node to be a part of our linked list.
            # Adding the first item in our list
            if curr is None:
                self._first = node
                curr = self._first
            # Otherwise, add this item to the tail of our list
            else:
                # Set next node to be this new node.
                curr.next = node
                curr = node
            # Increment the length, because we added a new node.
            self._length += 1
    # ------------------------------------------------------------------------
    # Methods from lecture/readings
    # ------------------------------------------------------------------------

    def is_empty(self) -> bool:
        """Return whether this linked list is empty.

        >>> GoatedList([]).is_empty()
        True
        >>> GoatedList([1, 2, 3]).is_empty()
        False
        """
        return self._first is None

    def __str__(self) -> str:
        """Return a string representation of this list in the form
        '[item1 -> item2 -> ... -> item-n]'.

        >>> str(GoatedList([1, 2, 3]))
        '[1 -> 2 -> 3]'
        >>> str(GoatedList([]))
        '[]'
        """
        items = []
        curr = self._first
        while curr is not None:
            items.append(str(curr.item))
            curr = curr.next
        return '[' + ' -> '.join(items) + ']'

    def __getitem__(self, index: Union[int, slice]) -> Union[Any, GoatedList]:
        """Return the item at position <index> in this list.

        Raise IndexError if <index> is >= the length of this list.

        >>> lst = GoatedList([1, 2, 10, 200])
        >>> lst[0]
        1
        >>> lst[-1]
        200
        >>> lst[-3]
        2
        >>> lst[-7]
        Traceback (most recent call last):
        IndexError
        >>> sliced = lst[0:2]
        >>> str(sliced)
        '[1 -> 2]'
        >>> sliced2 = lst[:]
        >>> str(sliced2)
        '[1 -> 2 -> 10 -> 200]'
        >>> sliced3 = lst[-1:]
        >>> str(sliced3)
        '[200]'
        >>> sliced4 = lst[-4:-1]
        >>> str(sliced4)
        '[1 -> 2 -> 10]'
        """
        target_index = None
        stop_index = None
        if isinstance(index, int):
            target_index = self._length + index if index < 0 else index

        # If it is a slice, need to change the target_index
        else:
            # Set it to the start index if it exists, otherwise 0
            target_index = index.start if index.start else 0
            stop_index = index.stop if index.stop else self._length

            # If it is negative, handle it.
            if target_index < 0:
                target_index = self._length + target_index
                # If it is negative, handle it.
            if stop_index < 0:
                stop_index = self._length + stop_index

        # If the negative index is _too_ negative.
        if target_index < 0:
            raise IndexError

        curr = self._first
        curr_index = 0
        while curr is not None and curr_index < target_index:
            curr = curr.next
            curr_index += 1

        assert curr is None or curr_index == target_index

        if curr is None:
            raise IndexError
        if isinstance(index, int):
            return curr.item

        # Inefficient way of doing it, but only uses a Linked List.
        # Otherwise, want to make a new GoatedList and return it.
        # gt = GoatedList([])

        # # Keep adding items until we reach the stop index O(n)
        # while curr is not None and curr_index < stop_index:
        #     # Insert the current node. O(n)
        #     gt.insert(curr_index - target_index, curr.item)
        #     curr = curr.next
        #     curr_index += 1

        # Efficient way of doing it, but uses a list as well.
        new_list = []
        # Keep adding items until we reach the stop index O(n)
        while curr is not None and curr_index < stop_index:
            # Insert the current node. O(1)
            new_list.append(curr.item)
            curr = curr.next
            curr_index += 1
        gt = GoatedList(new_list)  # O(n)
        return gt

    def insert(self, index: int, item: Any) -> None:
        """Insert the given item at the given index in this list.

        Raise IndexError if index > len(self) or index < 0.
        Note that adding to the end of the list is okay.

        >>> lst = GoatedList([1, 2, 10, 200])
        >>> lst.insert(2, 300)
        >>> str(lst)
        '[1 -> 2 -> 300 -> 10 -> 200]'
        >>> lst.insert(5, -1)
        >>> str(lst)
        '[1 -> 2 -> 300 -> 10 -> 200 -> -1]'
        >>> lst.insert(100, 2)
        Traceback (most recent call last):
        IndexError
        """
        # Create new node containing the item
        new_node = _Node(item)

        if index == 0:
            self._first, new_node.next = new_node, self._first
        else:
            # Iterate to (index-1)-th node.
            curr = self._first
            curr_index = 0
            while curr is not None and curr_index < index - 1:
                curr = curr.next
                curr_index += 1

            if curr is None:
                raise IndexError
            else:
                # Update links to insert new node
                curr.next, new_node.next = new_node, curr.next

        # Increment the length
        self._length += 1

    # ------------------------------------------------------------------------
    # Lab Task 1
    # ------------------------------------------------------------------------
    def __len__(self) -> int:
        """Return the number of elements in this list.

        >>> lst = GoatedList([])
        >>> len(lst)              # Equivalent to lst.__len__()
        0
        >>> lst = GoatedList([1, 2, 3])
        >>> len(lst)
        3
        """
        # # We want to find the number of nodes in our linked list!
        # # The only thing we have access to is self._first (first node in our list)
        # # Set some count variable.
        # length = 0
        # curr = self._first
        # # Loop through linked list, O(n)
        # while curr is not None:
        #     curr = curr.next
        #     # increment our length, we discovered a new node.
        #     length += 1

        # # Return the length that we computed.
        # return length
        return self._length

    def count(self, item: Any) -> int:
        """Return the number of times <item> occurs in this list.

        Use == to compare items.

        >>> lst = GoatedList([1, 2, 1, 3, 2, 1])
        >>> lst.count(1)
        3
        >>> lst.count(2)
        2
        >>> lst.count(3)
        1
        """
        # Count variable
        count = 0
        # loop tracking variable
        curr = self._first
        # Loop through linked list, O(n)
        while curr is not None:
            # Let's check if it is equal to the item.
            if curr.item == item:
                # If equal, increment the count
                count += 1
            curr = curr.next

        # Return the number of times that <item> occurs
        return count

    def index(self, item: Any) -> int:
        """Return the index of the first occurrence of <item> in this list.

        Raise ValueError if the <item> is not present.

        Use == to compare items.

        >>> lst = GoatedList([1, 2, 1, 3, 2, 1])
        >>> lst.index(1) 
        0
        >>> lst.index(3)
        3
        >>> lst.index(148)
        Traceback (most recent call last):
        ValueError
        """
        # index variable
        index = 0
        # loop tracking variable
        curr = self._first
        # Loop through linked list, O(n)
        while curr is not None:
            # Let's check if it is equal to the item.
            if curr.item == item:
                # If equal, return the current index, because we found the first occurrence.
                return index
            curr = curr.next
            index += 1

        # We did not find <item> in our linked list. So raise a ValueError
        raise ValueError

    def __setitem__(self, index: int, item: Any) -> None:
        """Store item at position <index> in this list.

        Raise IndexError if index >= len(self).

        >>> lst = GoatedList([1, 2, 3])
        >>> lst[0] = 100  # Equivalent to lst.__setitem__(0, 100)
        >>> lst[1] = 200
        >>> lst[2] = 300
        >>> str(lst)
        '[100 -> 200 -> 300]'
        """
        # index variable
        idx = 0
        # loop tracking variable
        curr = self._first
        # Loop through linked list, O(n)
        while curr is not None:
            # Let's check if we are at the index that we need to set at.
            if idx == index:
                # If equal, set the item of this _Node to <item>
                curr.item = item
                return
            curr = curr.next
            idx += 1
        # If we reach the end, then raise the IndexError because <index> >= len(self)
        raise IndexError


if __name__ == '__main__':
    # import python_ta
    # python_ta.check_all()
    import doctest
    doctest.testmod()
