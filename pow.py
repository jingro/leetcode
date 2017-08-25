class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1.0 / self.aux(x, -n)
        return self.aux(x, n)

    def aux(self, x, n):
        if not n:
            return 1
        t = self.aux(x, n / 2)
        if n % 2:
            return t * t * x
        return t * t
