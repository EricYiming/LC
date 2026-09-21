class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if target <= nums[0]: 
            return 0

        while l < r: 
            mid = (l + r + 1) // 2
            if nums[mid] > target: 
                r = mid - 1
            elif nums[mid] == target: 
                return mid
            else: 
                l = mid
        return l + 1