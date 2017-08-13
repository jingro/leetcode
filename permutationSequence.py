class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        a = [str(i) for i in range(1, n + 1)]
        res = []
        k -= 1
        fac = self.aux(n)
        for i in range(n, 1, -1):
            fac /= i
            t = k / fac
            res.append(a[t])
            a.pop(t)
            k %= fac
        res.append(a[0])
        return ''.join(res)

    def aux(self, n):
        res = 1
        for i in range(1, n + 1):
            res *= i
        return res
