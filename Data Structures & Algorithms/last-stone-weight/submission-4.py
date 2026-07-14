class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1: 
            return stones[0]
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        while len(heap) > 1: 
            first = -heapq.heappop(heap)
            second = -heapq.heappop(heap)
            if first != second: 
                heapq.heappush(heap, -(first - second))
        return -heap[0] if len(heap) != 0 else 0


        