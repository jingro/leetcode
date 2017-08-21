# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return False
        res = []
        results = []
        self.aux(root, sum, res, results)
        return results

    def aux(self, root, sum, res, results):
        if not root.left and not root.right:
            if sum == root.val:
                res.append(root.val)
                results.append(res[:])
                res.pop()
            return
        if root.left:
            res.append(root.val)
            self.aux(root.left, sum - root.val, res, results)
            res.pop()
        if root.right:
            res.append(root.val)
            self.aux(root.right, sum - root.val, res, results)
            res.pop()
