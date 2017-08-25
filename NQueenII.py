class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.cnt = 0
        pos = [0] * (2 * n - 1)
        main = [False] * (2 * n - 1)
        anti = [False] * (2 * n - 1)
        col = [False] * n
        self.aux(pos, 0, n, main, anti, col)
        return self.cnt

    def aux(self, pos, beg, n, main, anti, col):
        if beg == n:
            self.cnt += 1
            return
        for j in range(n):
            if col[j] or main[beg - j + n - 1] or anti[beg + j]:
                continue
            pos[beg] = j
            col[j] = main[beg - j + n - 1] = anti[beg + j] = True
            self.aux(pos, beg + 1, n, main, anti, col)
            col[j] = main[beg - j + n - 1] = anti[beg + j] = False


s = Solution()
print s.totalNQueens(10)
