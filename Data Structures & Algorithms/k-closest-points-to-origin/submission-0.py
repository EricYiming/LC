import math
class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points: 
            heap.append([self.dist(point), point])
        heapq.heapify(heap)
        res = []
        while k > 0: 
            item = heapq.heappop(heap)
            res.append(item[1])
            k -= 1
        return res

    def dist(self, points:List[int]): 
        return math.sqrt(points[0]**2 + points[1]**2)
        