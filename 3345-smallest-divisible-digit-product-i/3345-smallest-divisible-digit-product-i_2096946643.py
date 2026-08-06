class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, n+10):
            x = i
            prod = 1
            while x > 0:
                prod *= x % 10
                x //= 10
            if prod % t == 0:
                return i