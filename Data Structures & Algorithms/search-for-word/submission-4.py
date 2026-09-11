class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        MOVES = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n = len(word)
        num_row = len(board)
        num_col = len(board[0])


        def dfs(r, c, index): 
            if r < 0 or r >= num_row or c < 0 or c >= num_col or board[r][c] != word[index]: 
                return False
            if index == len(word) - 1: 
                return True
            flag = False
            temp = board[r][c]
            board[r][c] = '#'
            for move in MOVES: 
                nr = r + move[0]
                nc = c + move[1]
                flag = dfs(nr, nc, index + 1)
                if flag: 
                    return True
            board[r][c] = temp
            
            return False
        
        flag = False
        for r in range(num_row): 
            for c in range(num_col): 
                if board[r][c] == word[0]: 
                    flag = dfs(r, c, 0)
                    if flag: 
                        return True
        return False
            
            


        