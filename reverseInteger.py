class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1 if x > 0 else -1
        res = 0
        x = abs(x)
        limit = 0x7fffffff
        while x:
            t = x % 10
            res = res * 10 + t
            x /= 10
        if sign == 1 and res > limit:
            return 0
        elif sign == -1 and res > limit + 1:
            return 0
        return res * sign
