class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1:
            return n
        if n == 2:
            return 1
        fib = [0] * (n + 1)
        fib[0] = 0
        fib[1] = 1
        fib[2] = 1
        for i in range(3, n+1):
            fib[i] = fib[i-1] + fib[i-2] + fib[i-3]
        return fib[n]