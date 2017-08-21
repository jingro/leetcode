# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.aux(root)

    def aux(self, p):
        if not p.left and not p.right:
            return 1
        l = self.aux(p.left) if p.left else 2147483647
        r = self.aux(p.right) if p.right else 2147483647
        d = min(l, r)
        return d + 1
