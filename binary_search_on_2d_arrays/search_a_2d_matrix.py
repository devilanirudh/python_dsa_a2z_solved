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
        
        def column_searched(matrix, target):
            low = 0
            high = len(matrix) - 1  # Fixed: should be len(matrix) - 1
            ans = 0
            
            while low <= high:
                mid = (low + high) // 2
                if matrix[mid][-1] >= target:  # Fixed: use last element of row
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            
            # Boundary case 5: Check if the found row actually contains the target
            if matrix[ans][-1] < target:
                return -1  # Target not in any row
            return ans
        
        def row_searched(matrix, target, row_idx):
            # Boundary case 6: Invalid row index
            if row_idx < 0 or row_idx >= len(matrix):
                return False
            
            low = 0
            high = len(matrix[row_idx]) - 1  # Fixed: should be len(matrix[row_idx]) - 1
            ans = 0
            
            while low <= high:
                mid = (low + high) // 2
                if matrix[row_idx][mid] >= target:
                    ans = mid
                    high = mid - 1
                else:
                    low = mid + 1
            
            # Boundary case 7: Check if target exists at the found position
            if ans < len(matrix[row_idx]) and matrix[row_idx][ans] == target:
                return True
            return False
        
        # Boundary case 8: Handle case where column_searched returns -1
        row_idx = column_searched(matrix, target)
        if row_idx == -1:
            return False
        
        return row_searched(matrix, target, row_idx)
