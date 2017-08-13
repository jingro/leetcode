class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        r = False
        for i in range(n):
            if not matrix[0][i]:
                r = True
                break
        c = False
        for i in range(m):
            if not matrix[i][0]:
                c = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][j]:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if r:
            for j in range(n):
                matrix[0][j] = 0
        if c:
            for i in range(m):
                matrix[i][0] = 0






