class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(k // 2):
            top = x + i
            bottom = x + k - i - 1
            grid[top][y:y+k], grid[bottom][y:y+k] = grid[bottom][y:y+k], grid[top][y:y+k]
        return grid