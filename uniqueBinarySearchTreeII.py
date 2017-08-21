# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []
        return self.aux(1, n)

    def aux(self, beg, end):
        res = []
        if beg > end:
            return [None]
        for i in range(beg, end + 1):
            left = self.aux(beg, i - 1)
            right = self.aux(i + 1, end)
            for j in left:
                for k in right:
                    t = TreeNode(k)
                    t.left = j
                    t.right = k
                    res.append(t)
        return res
