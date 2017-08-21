# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        res = []
        self.aux(root, res)
        size = len(res)
        for i in range(size - 1):
            if res[i] >= res[i + 1]:
                return False
        return True

    def aux(self, p, res):
        if not p:
            return
        self.aux(p.left, res)
        res.append(p.val)
        self.aux(p.right, res)
