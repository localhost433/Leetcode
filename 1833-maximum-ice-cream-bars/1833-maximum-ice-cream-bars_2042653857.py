class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        MAX = 100000
        freq = [0] * (MAX + 1)
        for cost in costs:
            freq[cost] += 1
        ans = 0
        for cost in range(1, MAX + 1):
            if freq[cost] == 0:
                continue
            count = min(freq[cost], coins // cost)
            ans += count
            coins -= count * cost
            if coins < cost:
                break
        return ans