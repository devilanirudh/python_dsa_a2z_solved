class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.'] * n for _ in range(n)]
        ans = []

        def safe(r, c):
            # check column
            for i in range(r):
                if board[i][c] == 'Q':
                    return False
            
            # check left diagonal
            i, j = r-1, c-1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            # check right diagonal
            i, j = r-1, c+1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            
            return True

        def backtrack(r):
            if r == n:
                ans.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if safe(r, c):
                    board[r][c] = 'Q'
                    backtrack(r+1)
                    board[r][c] = '.'

        backtrack(0)
        return ans
