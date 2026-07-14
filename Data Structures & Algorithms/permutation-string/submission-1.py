class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s2_len = len(s2)

        def isPermutation(target, check): 
            t_freq = Counter(target)
            c_freq = Counter(check)
            for char, freq in t_freq.items(): 
                if char not in c_freq or c_freq[char] != freq: 
                    return False
            return True

        for i in range(s2_len - n + 1): 
            if isPermutation(s2[i: i + n], s1): 
                return True
        return False

        