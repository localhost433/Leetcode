class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        root = complexity[0]
        for i in range(1, len(complexity)):
            if complexity[i] <= root:
                return 0
        return math.factorial(len(complexity) - 1) % 1000000007