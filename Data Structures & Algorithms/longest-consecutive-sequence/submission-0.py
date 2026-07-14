class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set()
        for num in nums: 
            num_set.add(num)
        res = 0
        for num in nums: 
            count = 0
            cur = num
            if num-1 not in num_set: 
                count = 1
                while cur + 1 in num_set: 
                    count += 1
                    cur += 1
            
            res = max(count, res)
        return res
        