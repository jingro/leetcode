class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size < 2:
            return 0
        res = 0
        l = r = 0
        while l <= r:
            res += 1
            tr = r
            for i in range(l, r + 1):
                t = i + nums[i]
                if t >= size - 1:
                    return res
                if t > r:
                    r = t
            l = tr + 1
        return 0
