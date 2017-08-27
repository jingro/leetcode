class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        res = 0
        xx = x
        while xx:
            t = xx % 10
            res = res * 10 + t
            xx /= 10
        return x == res
