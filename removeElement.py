class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        size = len(nums)
        if not size:
            return size
        j = 0
        for i in range(size):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j
