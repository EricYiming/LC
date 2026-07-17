class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_row = len(matrix)
        num_col = len(matrix[0])

        l1, r1 = 0, num_row - 1
        while l1 < r1: 
            mid = (l1 + r1 + 1) // 2
            if matrix[mid][0] == target: 
                return True
            elif matrix[mid][0] > target: 
                r1 = mid - 1
            else: 
                l1 = mid
        
        l2, r2 = 0, num_col - 1
        
        while l2 <= r2: 
            mid = (l2 + r2) // 2
            val  = matrix[l1][mid]
            if val == target: 
                return True
            elif val < target: 
                l2 = mid + 1
            else: 
                r2 = mid - 1
            
        return False
            

        