class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        for i in range(n):
            ne = (startIndex + i) % n
            pr = (startIndex - i + n) % n
            if words[ne] == target or words[pr] == target:
                return i
        return -1