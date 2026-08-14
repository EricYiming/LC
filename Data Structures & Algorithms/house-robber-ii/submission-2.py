class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: 
            return nums[0]
        
        def rob_line(houses):
            prev1 = 0
            prev2 = 0

            for money in houses:
                current = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = current

            return prev1
        
        return max(rob_line(nums[0:n - 1]), rob_line(nums[1:n]))
        