class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs: 
            res += (str(len(s)) + "#" + s)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = j = 0
        n = len(s)
        while j < n: 
            if s[j] != "#": 
                j += 1
            else: 
                length = int(s[i:j])
                res.append(s[j + 1: j + 1 + length])
                i = j = j + 1 + length
            
        return res

