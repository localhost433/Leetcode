class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        arr = sorted(nums)
        if arr == nums:
            return 0
        n1, n2 = -1, -1
        for i in range(len(arr)):
            if arr[i] != nums[i]:
                if n1 == -1:
                    n1 = i
                n2 = i
        return abs(n2 - n1) + 1
            