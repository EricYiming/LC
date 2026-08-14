class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        res = [0] * (n + 1)
        res[0] = 0
        res[1] = nums[0]

        for i in range(2, n + 1): 
            res[i] = max(res[i - 1], res[i - 2] + nums[i - 1])
        return res[-1]
        