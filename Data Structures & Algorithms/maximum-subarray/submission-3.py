class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best = nums[0]
        running_sum = nums[0]
        for i in range(1,len(nums)): 
            running_sum = max(nums[i], nums[i] + running_sum)
            best = max(best, running_sum)
        return best

        