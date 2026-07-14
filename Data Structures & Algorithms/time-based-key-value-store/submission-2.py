class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)
        # map key to a sorted list based on timestamp
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((value, timestamp))
        

    def get(self, key: str, timestamp: int) -> str:

        search = self.cache[key]
        if len(search) == 0: 
            return ""

        left = 0
        right = len(search) - 1

        while left < right: 
            mid = left + (right - left) // 2+1
            mid_time = search[mid][1]
            if mid_time > timestamp: 
                right = mid - 1
            else: 
                left = mid
        return search[left][0] if search[left][1] <= timestamp else ""

        
