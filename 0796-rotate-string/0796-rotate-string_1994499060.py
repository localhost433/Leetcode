class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        g = len(goal)
        s += s
        while n == g:
            for i in range(n):
                if s[i:n+i] == goal:
                    return True
            return False
        return False