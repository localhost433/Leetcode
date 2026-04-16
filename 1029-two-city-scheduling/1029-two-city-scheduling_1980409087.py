class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs = sorted(costs, key=lambda x: (x[0] - x[1]))
        ret = 0
        n = len(costs)
        count = n
        for i in range(n // 2):
            ret += costs[i][0] + costs[n-i-1][1]
        return ret