class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        trip1 = trip2 = trip3 = False
        for a, b, c in triplets: 
            if a == target[0] and b <= target[1] and c <= target[2]: 
                trip1 = True
            if a <= target[0] and b == target[1] and c <= target[2]: 
                trip2 = True
            if a <= target[0] and b <= target[1] and c == target[2]: 
                trip3 = True
        return trip1 and trip2 and trip3
            