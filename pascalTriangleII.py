class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rowIndex += 1
        if not rowIndex:
            return []
        res = [1]
        for i in range(1, rowIndex):
            t = [1]
            for j in range(len(res) - 1):
                t.append(res[j] + res[j + 1])
            t.append(1)
            res = t
        return res
