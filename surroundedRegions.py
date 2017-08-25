class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        for j in range(n):
            self.aux(board, 0, j)
            self.aux(board, m - 1, j)
        for i in range(1, m - 1):
            self.aux(board, i, 0)
            self.aux(board, i, n - 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '+':
                    board[i][j] = 'O'

    def aux(self, board, i, j):
        q = []
        m, n = len(board), len(board[0])
        if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
            board[i][j] = '+'
            q.append((i, j))
        while len(q):
            i, j = q.pop(0)
            new = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
            for i, j in new:
                if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                    continue
                board[i][j] = '+'
                q.append((i, j))
