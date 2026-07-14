class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for time in times: 
            graph[time[0]].append((time[1], time[2]))
    
        dist = {i: float('inf') for i in range(1, n + 1)}
        dist[k] = 0

        pq = [(0, k)]

        while pq: 
            time, node = heapq.heappop(pq)

            if time > dist[node]: 
                continue
            
            for nei, nei_time in graph[node]: 
                new_time = nei_time + time
                if new_time < dist[nei]: 
                    dist[nei] = new_time
                    heapq.heappush(pq, (new_time, nei))
        
        max_time = float('-inf')
        for value in dist.values(): 
            if value == float('inf'): 
                return -1
            else: 
                max_time = max(max_time, value)
        return max_time