class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): 
            return -1
        net = []
        n = len(gas)
        for i in range(n): 
            net.append(gas[i] - cost[i])
        
        left, right = 0, 0
        total = 0
        for i in range(n): 
            total += net[right]
            if total < 0 : 
                left, right = (i + 1) % n , (i + 1) % n
                total = 0
            else: 
                right  = (right + 1) % n 
        return left
        