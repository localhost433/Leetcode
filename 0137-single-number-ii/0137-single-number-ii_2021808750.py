class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s = set()
        su = 0
        for num in nums:
            if num not in s:
                s.add(num)
                su += num
        return (su * 3 - sum(nums)) // 2