class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        detect = set()
        n = len(nums)
        for i, num in enumerate(nums): 
            if num in detect: 
                return True
            detect.add(num)
            if len(detect) > k: 
                detect.remove(nums[i - k])
            
        return False

        