class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        for u, v in prerequisites: 
            indegree[u] += 1
            adj[v].append(u)

        output = []
        q = deque()

        for i in range(numCourses): 
            if indegree[i] == 0: 
                q.append(i)
                output.append(i)
        
        while q: 
            node = q.popleft()
            
            neighbors = adj[node]
            for nei in neighbors: 
                indegree[nei] -= 1
                if indegree[nei] == 0: 
                    q.append(nei)
                    output.append(nei)
        if len(output) != numCourses: 
            return []
        return output

                
        