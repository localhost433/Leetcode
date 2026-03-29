class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            nums[i] = -nums[i]
        score = 0
        heapq.heapify(nums)
        for _ in range(k):
            val = -nums[0]
            if val == 0:
                break
            score += val
            heapq.heapreplace(nums, -((val + 2) // 3))
        return score