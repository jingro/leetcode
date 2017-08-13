class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = [0]
        for i in range(n):
            t = 1 << i
            for j in reversed(res):
                res.append(t | j)
        return res
