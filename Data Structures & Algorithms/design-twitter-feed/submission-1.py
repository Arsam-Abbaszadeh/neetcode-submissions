class Twitter:
    def __init__(self):
        self.follower = defaultdict(set)
        self.tweets = defaultdict(list)
        self.tweet_time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.tweet_time, tweetId))
        self.tweet_time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.follower[userId]:
            self.follow(userId, userId)
        
        userIds = self.follower[userId]
        idxs = {ids: (len(self.tweets[ids]) - 1) for ids in userIds}
        feed = []
        while len(feed) < 10:
            notAdded = True
            newest = -1
            newestId = -1
            newesI = -1
            for user in userIds:
                idx = idxs[user]
                if idx >= 0 and self.tweets[user][idx][0] > newest:
                    notAdded = False
                    newestId = user
                    newesI = idx
                    newest = self.tweets[user][idx][0]
            if notAdded:
                break
            feed.append(self.tweets[newestId][newesI][1])
            idxs[newestId] -= 1
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follower[followerId]:
            self.follower[followerId].remove(followeeId)
