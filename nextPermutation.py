class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        i = size - 2
        while i >= 0 and nums[i + 1] <= nums[i]:
            i -= 1
        if i == -1:
            nums.reverse()
            return
        for j in range(size - 1, i, -1):
            if nums[j] > nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                break
        t = nums[i + 1:]
        t.reverse()
        nums[i + 1:] = t
