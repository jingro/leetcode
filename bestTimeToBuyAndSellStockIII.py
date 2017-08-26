class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        if size < 2:
            return 0
        first = [0] * size
        second = [0] * size
        valley = prices[0]
        for i in range(1, size):
            valley = min(valley, prices[i])
            first[i] = max(first[i - 1], prices - valley)
        peak = prices[size - 1]
        for i in range(size - 2, -1, -1):
            peak = max(peak, prices[i])
            second[i] = max(second[i + 1], peak - prices[i])

        res = 0
        for i in range(size):
            res = max(first[i] + second[i])
        return res
