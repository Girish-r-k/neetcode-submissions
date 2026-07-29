class Twitter:

    
    def __init__(self):
        self.time = 0
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        heap = []

        self.followMap[userId].add(userId)

        for followee in self.followMap[userId]:
            if followee in self.tweetMap:
                index = len(self.tweetMap[followee]) - 1
                time, tweetId = self.tweetMap[followee][index]
                heapq.heappush(heap, (time, tweetId, followee, index - 1))

        while heap and len(res) < 10:
            time, tweetId, followee, index = heapq.heappop(heap)
            res.append(tweetId)

            if index >= 0:
                time, tweetId = self.tweetMap[followee][index]
                heapq.heappush(heap, (time, tweetId, followee, index - 1))

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId != followerId:
            self.followMap[followerId].discard(followeeId)