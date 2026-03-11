import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        proj = sorted(zip(capital, profits))
        max_heap = []
        idx = 0
        
        for _ in range(k):
            while idx < n and proj[idx][0] <= w:
                heapq.heappush(max_heap, -proj[idx][1])
                idx += 1
            if max_heap:
                w += -heapq.heappop(max_heap)
            else:
                break
        return w