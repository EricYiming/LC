class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(point1, point2): 
            x1 = point1[0]
            y1 = point1[1]
            x2 = point2[0]
            y2 = point2[1]
            return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

        heap = []
        for point in points: 
            heapq.heappush_max(heap, (distance(point, [0, 0]), point))
            if len(heap) > k: 
                heapq.heappop_max(heap)
        return [item[1] for item in heap ]
