class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxEnd = minEnd = nums[0]
        res = nums[0]

        for num in nums[1:]: 
            a = maxEnd * num
            b = minEnd * num
            maxEnd = max(num, a, b)
            minEnd = min(num, a, b)
            res = max(maxEnd, res)
        return res