class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_row = len(matrix)
        num_col = len(matrix[0])

        left, right = 0, num_row - 1
        while left < right: 
            mid = left + (right - left) // 2 
            mid_val = matrix[mid][-1]
            
            if mid_val == target: 
                return True
            elif mid_val < target: 
                left = mid + 1
            else: 
                right = mid
                
        l, r = 0, num_col - 1
        while l <= r: 
            mid = l + (r - l) // 2
            mid_val = matrix[left][mid]
            if mid_val == target: 
                return True
            elif mid_val < target: 
                l = mid + 1
            else: 
                r = mid - 1
        return False