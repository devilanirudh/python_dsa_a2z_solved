class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def recu(i,j,k):
            if k==len(word):
                return True
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
                return False
            if board[i][j] != word[k]:
                return False
            tmp = board[i][j]
            board[i][j] = '#'
            found = recu(i-1,j,k+1) or recu(i+1,j,k+1) or recu(i,j-1,k+1) or recu(i,j+1,k+1)
            board[i][j] = tmp
            return found
        def start():
            a = []
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if word[0]==board[i][j]:
                       if recu(i,j,0):
                            return True
            return False
        
        return start()
