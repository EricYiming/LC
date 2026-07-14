class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        count = 0
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites: 
            indegree[u] += 1
            adj[v].append(u)
        
        q = deque()
        for i in range(numCourses): 
            if indegree[i] == 0: 
                q.append(i)
                count += 1
        
        while q: 
            node = q.popleft()
            for nei in adj[node]: 
                indegree[nei] -= 1
                if indegree[nei] == 0: 
                    q.append(nei)
                    count += 1
        return count == numCourses
        
        
        
            
        