class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_seen = {}
        for i in range(len(s)): 
            c = s[i]
            last_seen[c] = i
        
        res = []
        prev_index = -1
        cur_index = 0
        for i in range(len(s)): 
            c = s[i]
            cur_index = max(cur_index, last_seen[c])
            if i == cur_index: 
                res.append(cur_index - prev_index)
                prev_index = cur_index
        return res
