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
        self.aux(root, None)

    def aux(self, root, sib):
        if not root:
            return
        else:
            root.next = sib
        self.aux(root.left, root.right)
        if sib:
            self.aux(root.right, sib.left)
        else:
            self.aux(root.right, None)