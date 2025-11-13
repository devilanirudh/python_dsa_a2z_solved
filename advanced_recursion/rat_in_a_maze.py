class Solution:
    def findPath(self, grid):
        a = []
        b = []
        def fp(i,j):
            if i>=len(grid) or j>=len(grid) or i<0 or j<0 or grid[i][j]==0:
                return
            if i==len(grid)-1 and j == len(grid)-1:
                a.append("".join(b))
                return
            
            grid[i][j]=0
            
            b.append('D')
            fp(i+1,j)
            b.pop()
            b.append('R')
            fp(i,j+1)
            b.pop()
            b.append('U')
            fp(i-1,j)
            b.pop()
            b.append('L')
            fp(i,j-1)
            b.pop()
            
            grid[i][j] = 1
              
        fp(0,0)
        return a
        
grid = [ [1, 0, 0, 0] , [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1] ]
print(Solution().findPath(grid))