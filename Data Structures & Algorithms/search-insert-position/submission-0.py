class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right: 
            mid = left + (right - left) // 2
            mid_val = nums[mid]
            if mid_val > target: 
                right = mid - 1
            elif mid_val < target: 
                left = mid + 1
            else: 
                return mid
        
        return left
        