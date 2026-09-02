class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = defaultdict(int)
        for c in s1: 
            target[c] += 1
        
        n = len(s1)
        m = len(s2)
        if m < n: 
            return False

        seen = defaultdict(int)
        for i in range(n): 
            seen[s2[i]] += 1

        for i in range(m - n):
            if target == seen: 
                return True
            
            seen[s2[i]] -= 1
            if seen[s2[i]] == 0: 
                del seen[s2[i]]
            seen[s2[i + n]] += 1
        
        return target == seen
            


        