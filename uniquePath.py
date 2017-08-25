class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        f = [0 for i in range(n)]
        f[0] = 1
        for i in range(m):
            for j in range(1, n):
                f[j] += f[j - 1]
        return f[n - 1]
