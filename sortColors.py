class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        r, b = 0, size - 1
        i = 0
        while i <= b:
            if not nums[i]:
                nums[i], nums[r] = nums[r], nums[i]
                r += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[b] = nums[b], nums[i]
                b -= 1
            else:
                i += 1




