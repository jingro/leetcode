class Solution(object):
    def romanToint(self, s):
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        i, size = 0, len(s)
        res = 0
        while i < size:
            if i < size - 1 and d[s[i]] < d[s[i + 1]]:
                res += (d[s[i + 1]] - d[s[i]])
                i += 2
            else:
                res += d[s[i]]
                i += 1
        return res
