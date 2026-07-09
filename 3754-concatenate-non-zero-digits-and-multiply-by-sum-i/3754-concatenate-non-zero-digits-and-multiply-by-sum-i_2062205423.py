class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = 0
        x = 0
        p = 1
        while n > 0:
            r = n % 10
            if r != 0:
                x += r * p
                s += r
                p *= 10
            n //= 10
        return x * s