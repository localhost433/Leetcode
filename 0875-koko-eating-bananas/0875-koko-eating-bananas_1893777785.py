class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        l = 1
        r = max(piles)
        def can(k: int):
            s = 0
            for p in piles:
                s += (p + k - 1) // k
                if s > h:
                    return False
            return True
        while l < r:
            k = (l + r) // 2
            if (can(k)):
                r = k
            else:
                l = k + 1
        return l