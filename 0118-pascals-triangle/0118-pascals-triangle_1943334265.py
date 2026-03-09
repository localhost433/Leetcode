class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1]*2]
        dp = [[1] * (i+1) for i in range(numRows)]
        for j in range(2, numRows):
            for k in range(1, j):
                dp[j][k] = dp[j-1][k-1] + dp[j-1][k]
        return dp