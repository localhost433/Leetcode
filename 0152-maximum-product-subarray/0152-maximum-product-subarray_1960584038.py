class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        it = iter(nums)
        try:
            first = next(it)
        except StopIteration:
            return 0
        ret = maxp = minp = first
        for n in it:
            if n < 0:
                maxp, minp = minp, maxp
            prod_max = n * maxp
            maxp = n if n > prod_max else prod_max
            prod_min = n * minp
            minp = n if n < prod_min else prod_min
            if maxp > ret:
                ret = maxp
        return ret