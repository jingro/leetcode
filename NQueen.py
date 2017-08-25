class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        pos = [0] * (2 * n - 1)
        main = [False] * (2 * n - 1)
        anti = [False] * (2 * n - 1)
        col = [False] * n
        self.aux(pos, 0, n, res, main, anti, col)
        return res

    def aux(self, pos, beg, n, results, main, anti, col):
        if beg == n:
            res = [['.' for j in range(n)] for i in range(n)]
            for i in range(n):
                res[i][pos[i]] = 'Q'
            results.append([''.join(i) for i in res])
            return
        for j in range(n):
            if col[j] or main[beg - j + n - 1] or anti[beg + j]:
                continue
            pos[beg] = j
            col[j] = main[beg - j + n - 1] = anti[beg + j] = True
            self.aux(pos, beg + 1, n, results, main, anti, col)
            col[j] = main[beg - j + n - 1] = anti[beg + j] = False
