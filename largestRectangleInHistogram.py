class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        size = len(heights)
        sta = []
        i, res = 0, 0
        while i < size:
            if not sta or heights[i] > heights[sta[-1]]:
                sta.append(i)
                i += 1
            else:
                t = sta.pop()
                res = max(res, heights[t] * (i if not sta else i - sta[-1] - 1))
        return res


solution = Solution()
x = [2, 1, 5, 6, 2, 3]

print solution.largestRectangleArea(x)
