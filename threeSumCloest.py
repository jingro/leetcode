class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        size = len(nums)
        res = []
        minT = 0x7fffffff
        nums.sort()
        for i in range(size - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, size - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                t = abs(sum - target)
                if not t:
                    return sum
                elif t < minT:
                    res = sum
                    minT = t
                elif t == 0:
                    return res
                if sum < target:
                    j += 1
                else:
                    k -= 1
        return res
