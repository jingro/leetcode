class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        visit = [[False for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if self.aux(board, word, 0, visit, i, j):
                    return True
        return False

    def aux(self, board, word, beg, visit, i, j):
        if beg == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return False
        if visit[i][j] or word[beg] != board[i][j]:
            return False
        visit[i][j] = True
        res = self.aux(board, word, beg + 1, visit, i - 1, j) \
              or self.aux(board, word, beg + 1, visit, i + 1, j) \
              or self.aux(board, word, beg + 1, visit, i, j - 1) \
              or self.aux(board, word, beg + 1, visit, i, j + 1)
        visit[i][j] = False
        return res
