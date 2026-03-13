class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        u = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[u]:
                u += 1
                nums[u] = nums[i]
        return u + 1
