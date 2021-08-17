class BTNode:
    """A node in a binary tree"""

    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class LLNode:
    """A node in a linked list"""

    def __init__(self, item, link):
        self.item = item
        self.link = link

    def __str__(self):
        s = str(self.item)
        if self.link:
            s += ' -> '
            s += str(self.link)
        return s


def preorder(root: BTNode) -> LLNode:
    """Return the first node in a linked list that contains every value from the
    binary tree rooted at root, listed according to a preorder traversal.
    >>> bt = BTNode(1, BTNode(2), BTNode(3))
    >>> str(preorder(bt))
    '1 -> 2 -> 3'
    >>> bst = BTNode(1, BTNode(2, BTNode(3), BTNode(4)), BTNode(5))
    >>> str(preorder(bst))
    '1 -> 2 -> 3 -> 4 -> 5'
    """
    # If theres no other trees, then just return this value
    if not (root.left or root.right):
        return LLNode(root.item, None)
    else:
        # Add root, then left, then right
        node = LLNode(root.item, None)
        left_node, right_node = None, None
        if root.left:
            left_node = preorder(root.left)
        if root.right:
            right_node = preorder(root.right)
        # Join the shit together.
        node.link = left_node
        # go to the end of left_node and then link up the right_node
        curr = left_node
        while curr.link:
            curr = curr.link
        # Now this is the last linked list node in our left subtrees recursive call
        curr.link = right_node
        return node


if __name__ == '__main__':
    import doctest
    doctest.testmod()
