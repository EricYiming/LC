class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count = Counter(hand)

        for num in hand: 
            start = num
            while count[start - 1]: 
                start = start - 1
            val = count[start]
            for i in range(start, start + groupSize): 
                count[i] -= val
                if count[i] < 0: 
                    return False
        for val, freq in count.items(): 
            if freq != 0: 
                return False
        return True

        
        
                
