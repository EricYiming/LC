class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        num_row, num_col = len(heights), len(heights[0])
        pac = [[0] * num_col for _ in range(num_row)]
        atl = [[0] * num_col for _ in range(num_row)]

        def dfs(r, c, pacific):
            if r < 0 or r >= num_row or c < 0 or c >= num_col: 
                return 
            if pacific and pac[r][c] == 1: 
                return
            elif not pacific and atl[r][c] == 1: 
                return 
            if pacific: 
                pac[r][c] = 1
            else: 
                atl[r][c] = 1
            
            moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for move in moves: 
                nr = r + move[0]
                nc = c + move[1]

                if 0 <= nr < num_row and 0 <= nc < num_col and heights[r][c] <= heights[nr][nc]:
                    
                    dfs(nr, nc, pacific)
        
        for r in range(num_row): 
            for c in range(num_col): 
                if r == 0 or c == 0:
                    dfs(r, c, True)
                if r == (num_row - 1) or c == (num_col - 1): 
                    dfs(r, c, False)

        res = []
        for r in range(num_row): 
            for c in range(num_col): 
                if pac[r][c] == 1 and atl[r][c] == 1: 
                    res.append([r, c])

        return res


            

        