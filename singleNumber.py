class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t = 0
        for i in nums:
            t ^= i
        return t
