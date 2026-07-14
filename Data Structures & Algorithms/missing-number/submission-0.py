class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = n + 1
        for num in nums: 
            res = res ^ num
        for i in range(n + 2): 
            res = res ^ i
        return res

        