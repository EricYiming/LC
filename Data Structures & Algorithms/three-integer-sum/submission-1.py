class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)
        for i in range(n): 
            if i > 0 and nums[i] == nums[i - 1]: 
                continue
            
            target = -nums[i]
            left = i + 1
            right = n - 1
            while left < right: 
                total = nums[left] + nums[right]
                if total < target: 
                    left += 1
                elif total > target: 
                    right -= 1
                else: 
                    res.append([nums[i], nums[left], nums[right]])
                    while left + 1 < n and nums[left] == nums[left + 1]: 
                        left += 1
                    left += 1
                    while right - 1 >= 0 and nums[right] == nums[right - 1]: 
                        right -= 1
                    right -= 1
        return res        