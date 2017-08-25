class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        if n > 0:
            self.aux(n, [], res, 0, 0)
        return res

    def aux(self, n, path, res, l, r):
        if l == n:
            t = ''.join(path)
            t += ')' * (n - r)
            res.append(t)
            return
        path.append('(')
        self.aux(n, path, res, l + 1, r)
        path.pop()

        if r < l:
            path.append(')')
            self.aux(n, path, res, l, r + 1)
            path.pop()
