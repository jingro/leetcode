# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        sta = []
        if root:
            sta.append(root)
        while len(sta):
            p = sta.pop()
            res.append(p.val)
            if p.right:
                sta.append(p.right)
            if p.left:
                sta.append(p.left)
        return res
