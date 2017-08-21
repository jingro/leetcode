# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        sta = []
        p = root
        while len(sta) or p:
            if p:
                sta.append(p)
                p = p.left
            else:
                p = sta.pop()
                res.append(p.val)
                p = p.right
        return res
