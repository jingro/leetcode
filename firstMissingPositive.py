class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        for i in range(size):
            while nums[i] != i + 1:
                if nums[i] <= 0 or nums[i] > size or nums[i] == nums[nums[i] - 1]:
                    break
                t = nums[i] - 1
                nums[i], nums[t] = nums[t], nums[i]
        for i in range(size):
            if nums[i] != i + 1:
                return i + 1
        return size + 1
