class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        MOVES = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        num_row = len(heights)
        num_col = len(heights[0])

        dist = defaultdict(lambda: float('inf'))
        dist[(0, 0)] = 0

        pq = [(0, 0, 0)]

        while pq: 
            distance, row, col = heapq.heappop(pq)

            if distance > dist[(row, col)]: 
                continue
            
            for move in MOVES: 
                nr = row + move[0]
                nc = col + move[1]
                if (0 <= nr < num_row) and (0 <= nc < num_col): 
                    new_distance = max(distance, abs(heights[nr][nc] - heights[row][col]))
                    if new_distance < dist[(nr, nc)]: 
                        dist[(nr, nc)] = new_distance
                        heapq.heappush(pq, (new_distance, nr, nc))
            
        return dist[(num_row - 1, num_col - 1)]
        