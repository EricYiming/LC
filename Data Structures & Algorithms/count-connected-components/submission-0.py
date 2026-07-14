class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        adj = [[] for _ in range(n)]
        for u, v in edges: 
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False] * n

        def dfs(i): 
            for nei in adj[i]: 
                if not visited[nei]: 
                    visited[nei] = True
                    dfs(nei)
        

        for i in range(n): 
            if not visited[i]: 
                visited[i] = True
                dfs(i)
                count += 1
        return count
        

        

