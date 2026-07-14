class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums: 
            if num in freq: 
                freq[num] += 1
            else: 
                freq[num] = 0
        
        arr = []
        for num, count in freq.items(): 
            arr.append([count, num])
        arr.sort()

        res = []
        while len(res) < k: 
            res.append(arr.pop()[1])
        return res
            
        