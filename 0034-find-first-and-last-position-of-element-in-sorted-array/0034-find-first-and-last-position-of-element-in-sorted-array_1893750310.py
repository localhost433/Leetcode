class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        start = 0
        end = n - 1
        if n == 0:
            return [-1, -1]
        while start <= end:
            if nums[start] == target and nums[end] == target:
                return [start, end]
            else:
                if nums[start] < target:
                    start += 1
                elif nums[end] > target:
                    end -= 1
                else:
                    start += 1
                    end -= 1
        return [-1, -1]