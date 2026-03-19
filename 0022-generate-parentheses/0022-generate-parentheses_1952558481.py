class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]
        for i in range(1, n + 1):
            for j in range(i):
                for l in dp[j]:
                    for r in dp[i-1-j]:
                        dp[i].append(f"({l}){r}")
        return dp[n]