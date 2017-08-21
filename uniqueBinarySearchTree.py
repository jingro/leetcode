class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = [0 for i in range(n + 1)]
        a[0] = a[1] = 1
        for i in range(2, n + 1):
            for j in range(i):
                a[i] += (a[j] * a[i - j - 1])
        return a[n]
