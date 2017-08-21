# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        while root:
            cur, prev = None, None
            while root:
                if not cur:
                    cur = root.left if root.left else root.right
                if root.left:
                    if prev:
                        prev.next = root.left
                    prev = root.left
                if root.right:
                    if prev:
                        prev.next = root.right
                    prev = root.right
                root = root.next
            root = cur
