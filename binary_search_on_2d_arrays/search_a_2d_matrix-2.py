from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Boundary case 1: Empty matrix
        if not matrix or not matrix[0]:
            return False
        
        # Boundary case 2: Single element matrix
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix[0][0] == target
        
        # Boundary case 3: Target is smaller than the smallest element
        if target < matrix[0][0]:
            return False
        
        # Boundary case 4: Target is larger than the largest element
        if target > matrix[-1][-1]:
            return False
        
        # For row-wise and column-wise sorted matrix, use the optimal approach:
        # Start from top-right corner and move based on comparison
        row = 0
        col = len(matrix[0]) - 1
        
        while row < len(matrix) and col >= 0:
            current = matrix[row][col]
            
            if current == target:
                return True
            elif current < target:
                # Current element is smaller, move down to next row
                row += 1
            else:
                # Current element is larger, move left to previous column
                col -= 1
        
        return False

a = Solution()
matrix=[[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 5
print(a.searchMatrix(matrix,target))