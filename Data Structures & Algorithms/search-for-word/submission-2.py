class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        num_row, num_col = len(board), len(board[0])
        n = len(word)
        flag = False

        def dfs(r, c, i): 
            if r < 0 or r >= num_row or c < 0 or c >= num_col or board[r][c] != word[i]: 
                return 
            if i == n - 1 and word[i] == board[r][c]: 
                nonlocal flag
                flag = True
                return
            
            else: 
                temp = board[r][c]
                board[r][c] = "#"
                dfs(r + 1, c, i + 1)
                dfs(r - 1, c, i + 1)
                dfs(r, c + 1, i + 1)
                dfs(r, c - 1, i + 1)
                board[r][c] = temp

        for r in range(num_row): 
            for c in range(num_col): 
                if board[r][c] == word[0]: 
                    dfs(r, c, 0)
        
        return flag
        
        