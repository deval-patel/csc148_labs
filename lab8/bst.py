"""Lab 8: Binary Search Trees

=== CSC148 Winter 2021 ===
Department of Mathematical and Computational Sciences,
University of Toronto Mississauga

=== Module Description ===
This module contains a few BinarySearchTree methods that you will implement.
Make sure you understand the *BST Property*; it will play an important role
in several of these methods.
"""
from __future__ import annotations
from typing import Any, List, Optional, Tuple
from queue import Queue


class BinarySearchTree:
    """Binary Search Tree class.

    This class represents a binary tree satisfying the Binary Search Tree
    property: for every item, its value is >= all items stored in its left
    subtree, and <= all items stored in its right subtree.
    """
    # === Private Attributes ===
    # The item stored at the root of the tree, or None if the tree is empty.
    _root: Optional[Any]
    # The left subtree, or None if the tree is empty.
    _left: Optional[BinarySearchTree]
    # The right subtree, or None if the tree is empty.
    _right: Optional[BinarySearchTree]

    # === Representation Invariants ===
    #  - If self._root is None, then so are self._left and self._right.
    #    This represents an empty BST.
    #  - If self._root is not None, then self._left and self._right
    #    are BinarySearchTrees.
    #  - (BST Property) If self is not empty, then
    #    all items in self._left are <= self._root, and
    #    all items in self._right are >= self._root.

    def __init__(self, root: Optional[Any]) -> None:
        """Initialize a new BST containing only the given root value.

        If <root> is None, initialize an empty tree.
        """
        if root is None:
            self._root = None
            self._left = None
            self._right = None
        else:
            self._root = root
            self._left = BinarySearchTree(None)
            self._right = BinarySearchTree(None)

    def is_empty(self) -> bool:
        """Return True if this BST is empty.

        >>> bst = BinarySearchTree(None)
        >>> bst.is_empty()
        True
        >>> bst = BinarySearchTree(10)
        >>> bst.is_empty()
        False
        """
        return self._root is None

    # -------------------------------------------------------------------------
    # Standard Container methods (search)
    # -------------------------------------------------------------------------
    def __contains__(self, item: Any) -> bool:
        """Return whether <item> is in this BST.

        >>> bst = BinarySearchTree(3)
        >>> bst._left = BinarySearchTree(2)
        >>> bst._right = BinarySearchTree(5)
        >>> 3 in bst
        True
        >>> 5 in bst
        True
        >>> 2 in bst
        True
        >>> 4 in bst
        False
        """
        if self.is_empty():
            return False
        elif item == self._root:
            return True
        elif item < self._root:
            return item in self._left   # or, self._left.__contains__(item)
        else:
            return item in self._right  # or, self._right.__contains__(item)

    # ------------------------------------------------------------------------
    # Deletion code from lecture (profiled in Task 3)
    # ------------------------------------------------------------------------
    def delete(self, item: Any) -> None:
        """Remove *one* occurrence of item from this BST.

        Do nothing if <item> is not in the BST.
        """
        if self.is_empty():
            pass
        elif self._root == item:
            self.delete_root()
        elif item < self._root:
            self._left.delete(item)
        else:
            self._right.delete(item)

    def delete_root(self) -> None:
        """Remove the root of this tree.

        Precondition: this tree is *non-empty*.
        """
        if self._left.is_empty() and self._right.is_empty():
            self._root = None
            self._left = None
            self._right = None
        elif self._left.is_empty():
            # "Promote" the right subtree.
            # Note that self = self._right does NOT work!
            self._root, self._left, self._right = \
                self._right._root, self._right._left, self._right._right
        elif self._right.is_empty():
            # "Promote" the left subtree.
            self._root, self._left, self._right = \
                self._left._root, self._left._left, self._left._right
        else:
            # Both subtrees are non-empty. Can shooe to replace the root
            # from either the max value of the left subtree, or the min value
            # of the right subtree. (Implementations are very similar.)
            self._root = self._left.extract_max()

    def extract_max(self) -> Any:
        """Remove and return the maximum item stored in this tree.

        Precondition: this tree is *non-empty*.
        """
        if self._right.is_empty():
            max_item = self._root
            # "Promote" the left subtree.
            # Alternate approach: call self.delete_root()!
            self._root, self._left, self._right = \
                self._left._root, self._left._left, self._left._right
            return max_item
        else:
            return self._right.extract_max()

    # -------------------------------------------------------------------------
    # Additional BST methods
    # -------------------------------------------------------------------------
    def __str__(self) -> str:
        """Return a string representation of this BST.

        This string uses indentation to show depth.
        """
        return self._str_indented(0)

    def _str_indented(self, depth: int) -> str:
        """Return an indented string representation of this BST.

        The indentation level is specified by the <depth> parameter.
        """
        if self.is_empty():
            return ''
        else:
            answer = depth * '  ' + str(self._root) + '\n'
            answer += self._left._str_indented(depth + 1)
            answer += self._right._str_indented(depth + 1)
            return answer

    # ------------------------------------------------------------------------
    # Task 1
    # ------------------------------------------------------------------------
    # TODO: implement this method!
    def height(self) -> int:
        """Return the height of this BST.

        >>> BinarySearchTree(None).height()
        0
        >>> bst = BinarySearchTree(7)
        >>> bst.height()
        1
        >>> bst._left = BinarySearchTree(5)
        >>> bst.height()
        2
        >>> bst._right = BinarySearchTree(9)
        >>> bst.height()
        2
        """
        if self.is_empty():
            return 0
        else:
            return 1 + max(self._left.height(), self._right.height())

    # TODO: implement this method!
    def items_in_range(self, start: Any, end: Any) -> List:
        """Return the items in this BST between <start> and <end>, inclusive.

        Precondition: all items in this BST can be compared with <start> and
        <end>.
        The items should be returned in sorted order.

        As usual, use the BST property to minimize the number of recursive
        calls.

        >>> bst = BinarySearchTree(7)
        >>> left = BinarySearchTree(3)
        >>> left._left = BinarySearchTree(2)
        >>> left._right = BinarySearchTree(5)
        >>> right = BinarySearchTree(11)
        >>> right._left = BinarySearchTree(9)
        >>> right._right = BinarySearchTree(13)
        >>> bst._left = left
        >>> bst._right = right
        >>> bst.items_in_range(4, 11)
        [5, 7, 9, 11]
        >>> bst.items_in_range(10, 13)
        [11, 13]
        """
        if self.is_empty():
            return []
        else:
            items = []
            # Add left subtree items
            items.extend(self._left.items_in_range(start, end))
            # Check if root is in range, if so, add it.
            if start <= self._root <= end:
                items.append(self._root)
            # Add right subtree items
            items.extend(self._right.items_in_range(start, end))
            return items

    # ------------------------------------------------------------------------
    # Task 2
    # ------------------------------------------------------------------------
    # TODO: implement this method!

    def insert(self, item: Any) -> None:
        """Insert <item> into this BST, maintaining the BST property.

        Do not change positions of any other nodes.

        >>> bst = BinarySearchTree(10)
        >>> bst.insert(3)
        >>> bst.insert(20)
        >>> bst._root
        10
        >>> bst._left._root
        3
        >>> bst._right._root
        20
        """
        # Add this item as the root
        if self.is_empty():
            self._root = item
            self._left = BinarySearchTree(None)
            self._right = BinarySearchTree(None)
        # Add this item to the left bst
        elif item < self._root:
            self._left.insert(item)
        # Add this item to the right bst
        else:
            self._right.insert(item)

    # ------------------------------------------------------------------------
    # Task 4
    # ------------------------------------------------------------------------

    def rotate_right(self) -> None:
        """Rotate the BST clockwise, i.e. make the left subtree the root.

        >>> bst = BinarySearchTree(7)
        >>> left = BinarySearchTree(3)
        >>> right = BinarySearchTree(11)
        >>> left._left = BinarySearchTree(2)
        >>> left._right = BinarySearchTree(5)
        >>> bst._left = left
        >>> bst._right = right
        >>> print(bst)
        7
          3
            2
            5
          11
        <BLANKLINE>
        >>> bst.rotate_right()
        >>> print(bst)
        3
          2
          7
            5
            11
        <BLANKLINE>
        >>> bst.rotate_right()
        >>> print(bst)
        2
          3
            7
              5
              11
        <BLANKLINE>
        """
        """
        Steps
        =====
        - Left child becomes the root
        - new_root.Right becomes old_root.Left
        - Old Root becomes The right of the new root (old left)
        """
        # If this tree or left subtree is empty, then we cannot do right rotation
        if self.is_empty() or self._left.is_empty():
            return
        # Step 1: Store the new root in a var
        new_root = self._left
        # Step 2: Store the old root in a var, update the current root
        old_root = BinarySearchTree(self._root)
        self._root = new_root._root
        old_root._left = new_root._right
        old_root._right = self._right
        # Step 3: Update the new Left and Right BSTs
        self._right = old_root
        self._left = new_root._left

    def rotate_left(self) -> None:
        """Rotate the BST counter-clockwise,
        i.e. make the right subtree the root.

        >>> bst = BinarySearchTree(7)
        >>> left = BinarySearchTree(3)
        >>> left._left = BinarySearchTree(2)
        >>> left._right = BinarySearchTree(5)
        >>> right = BinarySearchTree(11)
        >>> right._left = BinarySearchTree(9)
        >>> right._right = BinarySearchTree(13)
        >>> bst._left = left
        >>> bst._right = right
        >>> print(bst)
        7
          3
            2
            5
          11
            9
            13
        <BLANKLINE>
        >>> bst.rotate_left()
        >>> print(bst)
        11
          7
            3
              2
              5
            9
          13
        <BLANKLINE>
        >>> bst.rotate_left()
        >>> print(bst)
        13
          11
            7
              3
                2
                5
              9
        <BLANKLINE>
        """
        """
        Steps
        =====
        - Right child becomes the root
        - Right.Left becomes old_root.Right
        - Old Root becomes The left of the new root (old left)
        """
        # If this tree or right subtree is empty, then we cannot do left rotation
        if self.is_empty() or self._right.is_empty():
            return
        # Step 1: Store the new root in a var
        new_root = self._right
        # Step 2: Store the old root in a var, update the current root
        old_root = BinarySearchTree(self._root)
        self._root = new_root._root
        old_root._right = new_root._left
        old_root._left = self._left
        # Step 3: Update the new Left and Right BSTs
        self._right = new_root._right
        self._left = old_root

    def print_all_vals(self):
        # Create a queue to store bsts
        q = Queue()
        print(self._root)
        q.enqueue(self._left)
        q.enqueue(self._right)
        # Go through the queue and keep popping bsts
        while not q.is_empty():
            bst = q.dequeue()
            if bst._root:
                # Print the root val
                print(bst._root)
                # Enqueue it's children if it has them
                q.enqueue(bst._left)
                q.enqueue(bst._right)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    bst = BinarySearchTree(7)
    left = BinarySearchTree(3)
    left._left = BinarySearchTree(2)
    left._right = BinarySearchTree(5)
    right = BinarySearchTree(11)
    right._left = BinarySearchTree(9)
    right._right = BinarySearchTree(13)
    bst._left = left
    bst._right = right
    bst.print_all_vals()
    # import python_ta
    # python_ta.check_all()
