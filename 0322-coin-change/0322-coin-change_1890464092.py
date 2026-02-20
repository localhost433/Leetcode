class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        inf = amount + 1
        @lru_cache(None)
        def dfs(x: int) -> int:
            if x == 0:
                return 0
            if x < 0:
                return inf
            m = inf
            for coin in coins:
                m = min(m, dfs(x-coin)+1)
            return m

        ret = dfs(amount)
        return -1 if ret >= inf else ret