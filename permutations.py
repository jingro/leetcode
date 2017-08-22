class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.aux(nums, [], res)
        return res

    def aux(self, nums, t, res):
        if len(t) == len(nums):
            res.append(t[:])
            return
        for i in nums:
            if i in t:
                continue
            t.append(i)
            self.aux(nums, t, res)
            t.pop()
