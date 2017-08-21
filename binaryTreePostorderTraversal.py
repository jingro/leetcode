# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        sta = []
        p = root
        while True:
            while p:
                sta.append(p)
                p = p.left
            q = None
            while sta:
                p = sta.pop()
                if p.right == q:
                    res.append(p.val)
                    q = p
                else:
                    sta.append(p)
                    p = p.right
                    break
            if not sta:
                break
        return res
