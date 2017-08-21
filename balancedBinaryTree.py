# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.aux(root) >= 0

    def aux(self, p):
        if not p:
            return 0
        l = self.aux(p.left)
        r = self.aux(p.right)
        if l < 0 or r < 0 or abs(l - r) > 1:
            return -1
        return max(l, r) + 1
