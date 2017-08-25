class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2:
            return x
        l, r = 1, x
        while l <= r:
            mid = (l + r) / 2
            if x / mid == mid:
                return mid
            elif x / mid > mid:
                l = mid + 1
            else:
                r = mid - 1
        return r
