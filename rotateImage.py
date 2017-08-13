class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        size = len(matrix)
        for i in range(size / 2):
            matrix[i], matrix[size - i - 1] = matrix[size - i - 1], matrix[i]

        for i in range(size):
            for j in range(i, size):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]



solution = Solution()
matrix = [[1, 2], [3, 4]]
solution.rotate(matrix)
print matrix
