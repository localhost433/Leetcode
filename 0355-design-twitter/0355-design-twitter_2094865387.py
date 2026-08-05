import heapq

class Twitter:
    def __init__(self):
        self.user = {} # user: set(followees)
        self.tweets = {} # user: [(seq, tweet)]
        self.seq = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.seq += 1
        self.tweets.setdefault(userId, [])
        self.tweets[userId].append((self.seq, tweetId))
        if len(self.tweets[userId]) > 10:
            del self.tweets[userId][0]

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.user.get(userId, set())
        c = []
        for id in followees | {userId}:
            c.extend(self.tweets.get(id, []))
        c.sort(reverse=True)
        
        return [tweet for seq, tweet in c[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.user.setdefault(followerId, set()).add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.user:
            self.user[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)