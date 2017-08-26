class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = -0x7fffffff
        t = 0
        for i in nums:
            t = max(t + i, i)
            res = max(res, t)
        return res
