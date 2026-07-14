class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n): 
            target = 0 - nums[i]
            l = i + 1
            r = n - 1
            if i >0 and nums[i] == nums[i - 1]: 
                continue
            while l < r: 
                total = nums[l] + nums[r]
                if total < target: 
                    l += 1
                elif total > target: 
                    r -= 1
                else: 
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]: 
                        l += 1
                    while l < r and nums[r] == nums[r + 1]: 
                        r -= 1
        return res
                

        