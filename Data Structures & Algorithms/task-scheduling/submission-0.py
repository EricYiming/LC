class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0


        counter = Counter(tasks)
        maxheap = [-cnt for cnt in counter.values()]
        heapq.heapify(maxheap)

        q = deque()

        while q or maxheap: 
            if q: 
                freq, cool_finish = q[0]
                if time >= cool_finish: 
                    q.popleft()
                    heapq.heappush(maxheap, -freq)
            
            if maxheap: 
                temp = heapq.heappop(maxheap)
                freq = -temp
                freq -= 1
                if freq > 0: 
                    q.append((freq, time + n + 1))
            
            time += 1
        
        return time