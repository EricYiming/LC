class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = newInterval
        res = []
        flag = False
        for interval in intervals: 
            start, end = interval
            if end < s: 
                res.append(interval)
            elif start <= e: 
                s = min(s, start)
                e = max(e, end)
            else: 
                if not flag: 
                    res.append([s,e])
                    flag = True
                res.append(interval)
        if not flag: 
            res.append([s,e])
        return res
            