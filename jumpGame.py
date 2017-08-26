class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i, size = 0, len(nums)
        reach = 0
        while i <= reach and reach < size - 1:
            reach = max(reach, i + nums[i])
            i += 1
        return reach == size - 1
