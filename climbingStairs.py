class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        prev, cur = 1, 1
        for i in range(1, n):
            t = cur
            cur += prev
            prev = t
        return cur
