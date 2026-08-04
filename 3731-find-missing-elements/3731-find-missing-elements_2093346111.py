class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m = nums[0]
        n = nums[0]
        s = set()
        for i in nums:
            m = max(m, i)
            n = min(n, i)
            s.add(i)
        ret = []
        for j in range(n, m+1):
            if j not in s:
                ret.append(j)
        return ret