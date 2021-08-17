from __future__ import annotations
from typing import List, Any, Dict, Optional


class Queue:
    _data: Dict[int, Any]

    def __init__(self) -> None:
        """ Initialize an empty Queue """
        self._data = {}

    def to_multiset(self) -> List[Any]:
        """ Return a copy of the values in the Queue in an arbitrary order """
        return list(self._data.values())

    def is_empty(self) -> bool:
        """ Return True if there are no values in the Queue """
        if 0 not in self._data:
            return True
        return len(self._data[0]) == 0

    def enqueue(self, item: Any):
        # O(1)
        lst = self._data.setdefault(0, [])
        lst.append(item)

    def dequeue(self):
        # O(n)
        if 0 not in self._data:
            return None
        lst = self._data[0]
        item = lst.pop(0)
        # Update the data list again
        self._data[0] = lst
        return item


class TreeNode:
    '''A TreeNode ADT, that keeps track of a key and children of each node.
    === Public Attributes ===
    key: Optional[Any] The item stored at this tree's root, or None if the tree is empty.
    children: List[TreeNode] The list of all children of this tree.
    '''
    # === Representation Invariants ===
    # - If self.key is None then self.children is an empty list; this is an empty tree.
    # - If self.key is not None, and self.children is an empty list, this is a tree with just one node.

    def __init__(self, item: Optional[Any] = None, children: Optional[List[TreeNode]] = None):
        self.key = item
        if not children:
            self.children = []
        else:
            self.children = children[:]


def find_right_node(t: TreeNode, item: Any) -> Optional[TreeNode]:
    """Return the next node that occurs at the level where <item> occurs.
    If no such node exists, return None.
    Precondition: All values in the tree are unique.
    """
    if t is None:
        return None
    nodes = Queue()  # A queue to store nodes
    level_nums = Queue()  # Another queue to store node levels
    curr_level = 0
    nodes.enqueue(t)
    level_nums.enqueue(curr_level)
    while not nodes.is_empty():
        curr_node = nodes.dequeue()
        curr_level = level_nums.dequeue()
        # COMPLETE THE REST OF THE FUNCTION BELOW
        # Add all children
        for child in curr_node.children:
            nodes.enqueue(child)
            level_nums.enqueue(curr_level + 1)
        # If we found the item
        if curr_node.key == item and not nodes.is_empty():
            # The next node we find at the same level, is the one to return
            next_node = nodes.dequeue()
            next_level = level_nums.dequeue()
            if next_level == curr_level:
                return next_node


if __name__ == '__main__':
    # Testing find_right_node
    tree_nodes = [TreeNode(i) for i in range(1, 10)]
    # 1's children are 2, 3, 8, 9
    tree_nodes[0].children = [tree_nodes[1],
                              tree_nodes[2], tree_nodes[7], tree_nodes[8]]
    # 2's children are 4, 5
    tree_nodes[1].children = [tree_nodes[3], tree_nodes[4]]
    # 3's children are 6
    tree_nodes[2].children = [tree_nodes[5]]
    # 9's children are 7
    tree_nodes[8].children = [tree_nodes[6]]
    assert find_right_node(tree_nodes[0], 5) == tree_nodes[5]
    assert find_right_node(tree_nodes[0], 6) == tree_nodes[6]
    assert find_right_node(tree_nodes[0], 9) == None
