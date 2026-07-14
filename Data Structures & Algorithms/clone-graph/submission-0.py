"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: 
            return None

        new_graph = {}
        new_graph[node] = Node(node.val)
        q = deque([node])

        while q: 
            visited = q.popleft()
            for neighbor in visited.neighbors: 
                if neighbor not in new_graph: 
                    new_neigh = Node(neighbor.val)
                    new_graph[neighbor] = new_neigh
                    q.append(neighbor)
                new_graph[visited].neighbors.append(new_graph[neighbor])
                
        return new_graph[node]

                



        
