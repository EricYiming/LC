class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig_to_char = {
            '2': "abc", 
            '3': "def", 
            '4': "ghi", 
            '5': "jkl", 
            '6': "mno", 
            '7': "pqrs", 
            '8': "tuv", 
            '9': "wxyz"
        }
        res = []
        path = []
        n = len(digits)
        if n == 0: 
            return res

        def dfs(i): 
            if i == n: 
                res.append("".join(path))
                return 
            dig = digits[i]
            for char in dig_to_char[dig]: 
                path.append(char)
                dfs(i + 1)
                path.pop()
        dfs(0)
        return res
