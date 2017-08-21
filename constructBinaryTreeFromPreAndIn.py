# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.aux(preorder, inorder)

    def aux(self, preorder, inorder):
        if not preorder:
            return
        rootVal = preorder[0]
        root = TreeNode(rootVal)
        t = inorder.index(rootVal)

        root.left = self.aux(preorder[1: t + 1], inorder[:t])
        root.right = self.aux(preorder[t + 1:], inorder[t + 1:])
        return root
