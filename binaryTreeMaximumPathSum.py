# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = -2147483648
        res, t = self.aux(root, res)
        return res

    def aux(self, root, res):
        if not root:
            return res, 0
        res, l = self.aux(root.left, res)
        res, r = self.aux(root.right, res)
        t = root.val
        if l > 0:
            t += l
        if r > 0:
            t += r
        res = max(res, t)
        return res, max(l, r) + root.val if max(l, r) > 0 else root.val
