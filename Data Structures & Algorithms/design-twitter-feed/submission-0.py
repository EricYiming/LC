class Twitter:

    def __init__(self):
        self.time = 0
        self.subscribe = defaultdict(set)
        self.post = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.post[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        people = self.subscribe[userId]
        people.add(userId)

        max_heap = []
        for subscription in people: 
            for time, info in self.post[subscription]: 
                heapq.heappush(max_heap, (-time, info))
        
        res = []
        for i in range(10): 
            if len(max_heap) > 0: 
                res.append(heapq.heappop(max_heap)[1])
        return res



        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.subscribe[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.subscribe[followerId].discard(followeeId)
        
        
