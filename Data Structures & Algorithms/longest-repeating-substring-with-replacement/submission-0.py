class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        l = 0
        best = 0
        length = len(s)
        max_freq = 0 

        for r in range(length): 
            idx = ord(s[r]) - ord('A')
            freq[idx] += 1
            max_freq = max(freq[idx], max_freq)

            window_size = r - l + 1

            diff = window_size - max_freq

            if diff > k: 
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
                continue
            
            best = max(best, window_size)
        return best



            

        