class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        count = 0
        n = len(machines)
        s = sum(machines)
        if s % n != 0:
            return -1
        target = s // n
        cur = 0
        for d in machines:
            t = d - target
            cur += t
            count = max(count, abs(cur), t)
        return count