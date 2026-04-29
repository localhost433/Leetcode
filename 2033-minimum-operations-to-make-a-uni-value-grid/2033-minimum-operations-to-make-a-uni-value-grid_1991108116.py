class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        for row in grid:
            nums.extend(row)
        r = nums[0] % x
        for val in nums:
            if val % x != r:
                return -1
        nums.sort()
        m = nums[len(nums) // 2]
        
        ret = 0
        for val in nums:
            ret += abs(val - m) // x
            
        return ret