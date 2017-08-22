class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        self.aux(n, k, 1, 0, [], res)
        return res

    def aux(self, n, k, beg, d, res, results):
        if d + n - beg + 1 < k:  # to avoid TLE: d equals the number of items already in res
            return
        if d == k:
            results.append(res[:])
            return
        for i in range(beg, n + 1):
            res.append(i)
            self.aux(n, k, i + 1, d + 1, res, results)
            res.pop()
