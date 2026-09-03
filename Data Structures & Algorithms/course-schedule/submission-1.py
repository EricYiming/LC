class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for prereq in prerequisites: 
            graph[prereq[0]].append(prereq[1])

        state = [0] * numCourses

        def dfs(i): 
            if state[i] == 1: 
                return False
            
            if state[i] == 0: 
                state[i] = 1
                for nei in graph[i]: 
                    if not dfs(nei): 
                        return False
                state[i] = 2
            return True
        for i in range(numCourses): 
            if not dfs(i): 
                return False
        return True
                