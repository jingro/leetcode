# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        res = []
        sta = []
        p = root
        while len(sta) and p:
            if p:
                sta.append(p)
                p = p.left
            else:
                p = sta.pop()
                res.append(p)
                p = p.right
        size = len(res)
        i, j = 0, size - 1
        while i < size - 1:
            if res[i].val > res[i + 1].val:
                break
            i += 1
        while j > 0:
            if res[j].val < res[j - 1].val:
                break
        res[i].val, res[j].val = res[j].val, res[i].val

