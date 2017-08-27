class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if not numRows:
            return []
        res = [[1]]
        for i in range(1, numRows):
            t = [1]
            for j in range(len(res[i - 1]) - 1):
                t.append(res[i - 1][j] + res[i - 1][j + 1])
            t.append(1)
            res.append(t)
        return res
