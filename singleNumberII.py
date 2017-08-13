class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = b = c = 0
        for i in nums:
            b |= (a & i)
            a ^= i
            c = ~(a & b)
            a &= c
            b &= c
        return a
