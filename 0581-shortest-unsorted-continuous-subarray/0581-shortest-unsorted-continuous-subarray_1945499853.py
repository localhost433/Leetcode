class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        low, high = 0, -1
        max_val = nums[0]
        for i in range(1, n):
            if nums[i] < max_val:
                high = i
            else:
                max_val = nums[i]
                
        min_val = nums[n-1]
        for i in range(n-2, -1, -1):
            if nums[i] > min_val:
                low = i
            else:
                min_val = nums[i]
        
        return high - low + 1