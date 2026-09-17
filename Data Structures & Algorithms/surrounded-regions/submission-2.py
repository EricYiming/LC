class Solution:
    def solve(self, board: List[List[str]]) -> None:
        num_row = len(board)
        num_col = len(board[0])
        MOVES = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def dfs(r, c): 
            if r < 0 or r >= num_row or c < 0 or c >= num_col or board[r][c] != 'O': 
                return
            board[r][c] = 'T'
            for move in MOVES: 
                nr = r + move[0]
                nc = c + move[1]
                dfs(nr, nc)
        
            return
        
        for r in range(num_row): 
            if board[r][0] == 'O': 
                dfs(r, 0)
            if board[r][num_col - 1] == 'O': 
                dfs(r, num_col - 1)
        for c in range(num_col): 
            if board[0][c] == 'O': 
                dfs(0, c)
            if board[num_row - 1][c] == 'O': 
                dfs(num_row - 1, c)
        
        for r in range(num_row): 
            for c in range(num_col): 
                if board[r][c] == 'O': 
                    board[r][c] = 'X'
                elif board[r][c] == 'T': 
                    board[r][c] = 'O'
        
            
            
            