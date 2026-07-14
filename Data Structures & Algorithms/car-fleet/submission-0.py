class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count = 0
        cars = sorted(zip(position, speed))
        position, speed = map(list, zip(*cars)) if cars else ([], [])
        n = len(position) 
        p1, p2 = n - 1, n - 1

        while p1 >= 0: 
            vp1 = speed[p1]
            vp2 = speed[p2]
            pp1 = position[p1]
            pp2 = position[p2]
            diff = pp2 - pp1
            vdiff = vp1 - vp2
            if vdiff <= 0: 
                count += 1
                p2 = p1
                p1 -= 1
                continue
            time = float(diff) / float(vp1 - vp2)
            catch = pp2 + vp2 * time
            if catch > target: 
                count += 1
                p2 = p1
                p1 -= 1
                continue
            else: 
                p1 -= 1
        return count


                

