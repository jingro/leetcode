# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.aux(inorder, postorder)

    def aux(self, inorder, postorder):
        if not inorder:
            return
        rootVal = postorder[-1]
        root = TreeNode(rootVal)
        t = inorder.index(rootVal)

        root.left = self.aux(inorder[:t], postorder[:t])
        root.right = self.aux(inorder[t + 1:], postorder[t: -1])
        return root
