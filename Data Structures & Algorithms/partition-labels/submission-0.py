class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        occur = {}
        for i, c in enumerate(s): 
            occur[c] = i
        n = len(s)
        res = []
        max_index = 0
        cur = 0
        count = 0
        while cur < n: 
            while cur <= max_index: 
                c = s[cur]
                max_index = max(max_index, occur[c])
                cur += 1
                count += 1
            res.append(count)
            count = 0
            max_index = cur
        return res
        

        
            
        