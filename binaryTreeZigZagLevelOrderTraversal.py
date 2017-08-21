# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        q = []
        if root:
            q.append((root, 1))
        res = []
        while len(q):
            p, d = q.pop(0)
            if len(res) < d:
                res.append([p.val])
            elif d % 2:
                res[d - 1].append(p.val)
            else:
                res[d - 1].insert(0, p.val)
            if p.left:
                q.append((p.left, d + 1))
            if p.right:
                q.append((p.right, d + 1))
        return res
