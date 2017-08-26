class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        res = 0
        m, n = len(matrix), len(matrix[0])
        H = [0] * n
        L = [0] * n
        R = [n] * n
        for i in range(m):
            l, r = 0, n
            for j in range(n):
                if matrix[i][j] == '1':
                    H[j] += 1
                    L[j] = max(L[j], l)
                else:
                    l = j + 1
                    H[j] = 0
                    L[j] = 0
                    R[j] = n
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    R[j] = min(R[j], r)
                    res = max(res, H[j] * (R[j] - L[j]))
                else:
                    r = j
        return res
