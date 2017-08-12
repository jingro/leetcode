class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size < 3:
            return size
        j = 0
        for i in range(2, size):
            if nums[i] != nums[j]:
                nums[j + 2] = nums[i]
                j += 1
        return j + 2
