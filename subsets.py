class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.aux(nums, 0, [], res)
        return res

    def aux(self, nums, beg, res, results):
        results.append(res[:])
        for i in range(beg, len(nums)):
            res.append(nums[i])
            self.aux(nums, i + 1, res, results)
            res.pop()
