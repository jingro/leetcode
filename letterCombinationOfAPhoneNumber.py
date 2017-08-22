class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not len(digits):
            return []
        a = [' ', '*', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        results = []
        self.aux(digits, 0, '', results, a)
        return results

    def aux(self, digits, d, res, results, a):
        if d == len(digits):
            results.append(res)
            return
        t = int(digits[d])
        for i in a[t]:
            self.aux(digits, d + 1, res + i, results, a)
