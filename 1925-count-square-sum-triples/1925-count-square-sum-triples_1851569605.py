class Solution:
    def countTriples(self, n: int) -> int:
        squares = [i*i for i in range(n+1)]
        square_set = set(squares[:])
        ans = 0
        for a in range(1, n+1):
            for b in range(1, n+1):
                if squares[a] + squares[b] in square_set:
                    ans += 1
        return ans