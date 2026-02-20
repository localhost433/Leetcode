class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        run = 0
        ret = []
        for bit in nums:
            run = (run * 2 + bit) % 5
            ret.append(run == 0)
        return ret
