class Solution:
    def maxProduct(self, n: int) -> int:
        p = 0
        m = 0
        while n > 0:
            num = n % 10
            n //= 10
            if num >= m:
                p = m
                m = num
            elif num > p:
                p = num
        return m * p            
        