class Twitter:

    def __init__(self):
        self.clock = 0
        self.follow_list = defaultdict(set) # account -> list of account id
        self.account_tweets = defaultdict(set) # account -> list of tweet ids

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.account_tweets[userId].add((self.clock, tweetId))
        self.clock += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        temp = []
        for f_id in self.follow_list[userId]:
            for tweet in self.account_tweets[f_id]:
                temp.append(tweet)
        temp.extend(self.account_tweets[userId])
        temp.sort(reverse=True)
        return [tweet for _, tweet in temp[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_list[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_list[followerId]: self.follow_list[followerId].remove(followeeId) 