class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: 
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    def helper(self, nums):
        n = len(nums)
        res = [0] * n
        res[0] = nums[0]
        if n > 1: 
            res[1] = max(nums[0], nums[1]) 
        for i in range(2, n): 
            res[i] = max(nums[i] + res[i - 2], res[i - 1])  
        return res[-1]     
            