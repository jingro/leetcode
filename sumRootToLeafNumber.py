# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.aux(root, 0)

    def aux(self, root, res):
        if not root:
            return 0
        if not root.left and not root.right:
            return res * 10 + root.val
        return self.aux(root.left, res * 10 + root.val) + self.aux(root.right, res * 10 + root.val)
