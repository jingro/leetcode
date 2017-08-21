# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        lo, hi = 0, len(nums) - 1
        return self.aux(nums, lo, hi)

    def aux(self, nums, lo, hi):
        if lo > hi:
            return
        mid = (lo + hi) / 2
        root = TreeNode(nums[mid])
        root.left = self.aux(nums, lo, mid - 1)
        root.right = self.aux(nums, mid + 1, hi)
        return root
