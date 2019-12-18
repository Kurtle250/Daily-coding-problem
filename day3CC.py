"""
Given the root to a binary tree, implement serialize(root),
which serializes the tree into a string, and deserialize(s),
which deserializes the string back into the tree.
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):

    if root is None:
        return ""

    def traverse(node):
    # Helper function to fill tree with delimiter(*)
        if node:
            temp.append(str(node.val))
            traverse(node.left)
            traverse(node.right)
        else:
            temp.append("*")
    temp = []
    traverse(root)
    return " ".join(temp)

def deserialize(s):
    def builder():
    # Helper function to rebuild pre-ordered binary tree
        val = next(temp)
        if val == "*":
            return None;
        node = Node(int(val))
        node.left = build()
        node.right = build()
        return node
    temp = iter(s.split())
    return build()
