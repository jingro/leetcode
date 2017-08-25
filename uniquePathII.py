class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if not obstacleGrid:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[0][0] or obstacleGrid[m - 1][n - 1]:
            return 0
        f = [0 for i in range(n)]
        f[0] = 1
        for i in range(m):
            f[0] = 0 if not f[0] else 0 if obstacleGrid[i][0] else f[0]
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    f[j] = 0
                else:
                    f[j] += f[j - 1]
        return f[n - 1]
