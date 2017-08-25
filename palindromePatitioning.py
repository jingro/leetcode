class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        if not s:
            return []
        self.aux(s, [], res, 0)
        return res

    def aux(self, s, path, res, beg):
        if beg == len(s):
            res.append(path[:])
            return
        for i in range(beg, len(s)):
            t = s[beg:i + 1]
            if t == t[::-1]:
                path.append(t)
                self.aux(s, path, res, i + 1)
                path.pop()
