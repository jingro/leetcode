class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size = len(nums)
        if size < 2:
            return []
        d = {}
        for i in range(size):
            if nums[i] not in d:
                d[target - nums[i]] = i
            else:
                return [d[nums[i]], i]
