class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = {}
        for i in nums:
            if i not in d:
                d[i] = False
        res = 0
        for i in nums:
            if d[i]:
                continue
            cnt = 0
            j = i
            while j in d:
                cnt += 1
                d[j] = True
                j += 1
            j = i - 1
            while j in d:
                cnt += 1
                d[j] = True
                j -= 1
            res = max(res, cnt)
        return res
