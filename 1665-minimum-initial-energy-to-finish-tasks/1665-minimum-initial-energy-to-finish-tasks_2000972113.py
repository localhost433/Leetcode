class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key = lambda x: x[1] - x[0], reverse = True)
        ans = 0
        cur = 0
        for actual, minimum in tasks:
            ans = max(ans, cur + minimum)
            cur += actual
        return ans