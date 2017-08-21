# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        return self.aux(root, sum)

    def aux(self, root, sum):
        if not root.left and not root.right:
            return sum == root.val
        l = self.aux(root.left, sum - root.val) if root.left else False
        r = self.aux(root.right, sum - root.val) if root.right else False
        return l or r


