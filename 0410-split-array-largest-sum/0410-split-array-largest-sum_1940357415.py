class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        ret = high
        while low <= high:
            mid = (low + high) // 2
            if self.canSplit(nums, k, mid):
                ret = mid
                high = mid - 1
            else:
                low = mid + 1
        return ret

    def canSplit(self, nums, k, max_sum):
        count = 1
        cur = 0
        for num in nums:
            if cur + num > max_sum:
                count += 1
                cur = num
                if count > k:
                    return False
            else:
                cur += num
        return True