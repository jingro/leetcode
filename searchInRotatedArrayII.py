class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        lo, hi = 0, size - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            if nums[mid] == target:
                return True
            elif nums[lo] < nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            elif nums[lo] > nums[mid]:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
            else:
                lo += 1
        return False
