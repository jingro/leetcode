class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        size = len(height)
        if size < 3:
            return 0
        res = 0
        left, right = height[0], height[size - 1]
        i, j = 0, size - 1
        while i < j:
            left = max(left, height[i])
            right = max(right, height[j])
            if left <= right:
                res += (left - height[i])
                i += 1
            else:
                res += (right - height[j])
                j -= 1
        return res
