class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(n-1):
            cur = ratings[i+1]
            prev = ratings[i]
            if cur > prev:
                candies[i+1] = candies[i] + 1
        for i in range(n-2, -1, -1):
            prev = ratings[i+1]
            cur = ratings[i]
            if cur > prev:
                candies[i] = max(candies[i], candies[i+1] + 1)
        return sum(candies)