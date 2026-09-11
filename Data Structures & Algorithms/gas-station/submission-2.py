class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): 
            return -1
        n = len(gas)
        surplus = [0] * n
        for i in range(n): 
            surplus[i] = gas[i] - cost[i]
        index = 0
        tot = 0
        for i in range(n): 
            tot += surplus[i]
            if tot < 0: 
                index = i + 1
                tot = 0
            
        return index

        