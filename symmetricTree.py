# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.aux(root.left, root.right)

    def aux(self, p, q):
        if not p or not q:
            return True
        elif (p and not q) or (q and not p):
            return False
        return p.val == q.val and self.aux(p.left, q.right) and self.aux(p.right, q.left)
