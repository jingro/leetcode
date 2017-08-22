class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        lo, hi = 0, m * n - 1
        while lo <= hi:
            mid = (lo + hi) / 2
            val = matrix[mid / n][mid % n]
            if target > val:
                lo = mid + 1
            elif target < val:
                hi = mid - 1
            else:
                return True
        return False


m = []
solution = Solution()
print solution.searchMatrix(m, 2)
