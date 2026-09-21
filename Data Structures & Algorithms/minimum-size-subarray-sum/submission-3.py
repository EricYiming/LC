class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        res = len(nums)
        if sum(nums) < target: 
            return 0
        
        for i in range(len(nums)): 
            total += nums[i]

            while total >= target: 
                res = min(res, i - l + 1)
                total -= nums[l]
                l += 1
        return res
                
        
