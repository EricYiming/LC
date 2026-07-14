class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        num_row = len(board)
        num_col = len(board[0])

        def push_if_O(r, c): 
            if (0 <= r < num_row) and (0 <= c < num_col) and board[r][c] == 'O': 
                q.append((r, c))
                board[r][c] = "#"
            
        for r in range(num_row): 
            push_if_O(r, 0)
            push_if_O(r, num_col - 1)
        for c in range(num_col): 
            push_if_O(0, c)
            push_if_O(num_row - 1, c)
        
        while q: 
            r, c = q.popleft()
            push_if_O(r, c + 1)
            push_if_O(r, c - 1)
            push_if_O(r + 1, c)
            push_if_O(r - 1, c)
        
        for r in range(num_row): 
            for c in range(num_col): 
                if board[r][c] == "O": 
                    board[r][c] = "X"
                elif board[r][c] == '#':
                    board[r][c] = "O"
         

        

        