# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.aux(root)

    def aux(self, p):
        if not p:
            return 0
        l = self.aux(p.left)
        r = self.aux(p.right)
        d = max(l, r)
        return d + 1
