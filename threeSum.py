class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        res = []
        nums.sort()
        for i in range(size - 2):
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            j, k = i + 1, size - 1
            while j < k:
                t = nums[i] + nums[j] + nums[k]
                if not t:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1] and nums[k] == nums[k + 1]:
                        j += 1
                        k -= 1
                elif t < 0:
                    j += 1
                else:
                    k -= 1
        return res
