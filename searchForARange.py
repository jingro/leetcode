class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if target > nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        i = lo
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if target >= nums[mid]:
                lo = mid + 1
            else:
                hi = mid - 1
        j = hi
        if nums[j] != target:
            return -1, -1
        return i, j
